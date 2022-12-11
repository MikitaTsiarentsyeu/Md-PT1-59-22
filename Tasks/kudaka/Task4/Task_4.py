print("your text is :\n")
with open("text.txt", "r") as show:
    print(show.read()+"\n")
while True:
    user = input("How many characters do you want in one row?\nchoose above 35 : ")
    if user.isnumeric() and int(user) > 35:
        user_num = int(user)
        break
    else:
        print("some thing is wrong,please try again")

def prinit(value):
    with open("text_copy.txt", "a") as prn_text:
        prn_text.write(value+"\n")

def make_35(string):
    count_pb = string.count(" ")
    num = 2
    count_1 = 0
    count_3 = 0
    while len(string) != user_num:
        index = string[count_1:].index(" ")
        string = string[:index+count_1] + " " + string[index+count_1:]
        count_1 += index + num
        count_3 += 1
        if count_pb == count_3:
            num += 1
            count_1 = 0
            count_3 = 0
    return string

with open("text.txt","r") as text:
    count_2 = 0
    while True:
        count = user_num +1
        text.seek(count_2)
        t = text.read(count)
        if len(t) < count:
            if t[0] != " " and t[-1] != " ":
                prinit(t)
                break
            else:
                result = make_35(t.strip(" "))
                prinit(result)
                break
        elif t[-1] == " " or t[-1] == "\n":
            words = (t[:count].replace("\n"," ").strip(" "))
            prinit(words)
            count_2 += count
        elif t[-1] != " " or t[-1] != "\n":
            while True:
                count -= 1
                if t[count] == " " or t[count] == "\n":
                    break
            words = (t[:count].replace("\n"," ").strip(" "))
            result = make_35(words)
            prinit(result)
            count_2 += count+1

with open("text_copy.txt", "r") as prn_text:
    print("your file was writen as text_copy,and result is:\n")
    print(prn_text.read())