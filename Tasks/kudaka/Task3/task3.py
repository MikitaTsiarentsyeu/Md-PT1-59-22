import time
str_time = ""
list_time = list(str_time)
number_dic = {0: "midnight", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
              9: "nine",
              10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
              17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty"}
def time_print(*args):
    h_count = args[0]
    m_count = args[1]
    time = args[2]
    i = args[3]
    list_time = list(str_time)
    list_time[-1] = 0
    clear_m = str(list_time[-2]) + str(list_time[-1])

    if m_count < 30:
        if m_count > 20:
            print(
                f"{time} It’s {number_dic[int(clear_m)]}-{number_dic[int(time[-1])]} past {number_dic[h_count]} {i}")
        elif m_count <= 20:
            print(f"{time} It's {number_dic[m_count]} past {number_dic[h_count]} {i}")
    elif m_count > 30 and m_count < 45:
        if m_count > 20:
            print(
                f"{time} It’s {number_dic[int(clear_m)]}-{number_dic[int(time[-1])]} minutes past {number_dic[h_count]} {i}")
        elif m_count <= 20:
            print(f"{time} It's {number_dic[m_count]} minute past {number_dic[h_count]} {i}")
    elif m_count >= 45:
        c_time = 60 - int(time[-2:])
        print(f"{time} It's without {number_dic[c_time]} minute {number_dic[h_count +1]} {i}")



def const_num(time):
    h_count = int(time[0:2])
    m_count = int(time[-2:])
    if h_count > 12:
        h_count -= 12
        if m_count == 0:
            print(f"{time} it’s exactly {number_dic[h_count]} hours pm.")
        else:
            time_print(h_count, m_count, time,"pm.")
    elif h_count == 0:
        if m_count == 0:
            print(f"{time} it's exactly midnight")
        else:
            time_print(h_count, m_count, time,"")
    elif h_count <= 12:
        if m_count == 0 and h_count == 12:
            print(f"{time} it’s exactly noon")
        elif m_count == 0:
            print(f"{time} it’s exactly {number_dic[h_count]} hours am.")
        else:
            time_print(h_count, m_count, time,"am.")


def time_bloc():
    time_ob = time.localtime()
    comp_time = time.strftime("%H:%M", time_ob)
    print("Local time is " + comp_time)
    return comp_time


def time_representation(time):
    loc_time = time_bloc()
    if not time:
        time = loc_time
    global str_time
    str_time += time[0:2]+time[-2:]
    const_num(time)

time_bloc()
while True:
    user_yes_no = input("Do you want to type the time by yourself?\nAnswear (y/n):\n")
    if user_yes_no.lower() == "y":
        while True:
            user_time_ = input("Please enter time expressed in hours and minutes in format HH:MM\n")
            count = 0
            for i in user_time_.split(":"):
                if i.isnumeric() and int(i) >= 0 and int(i) < 24 and count == 0:
                    count += 1
                    continue
                if i.isnumeric() and int(i) >= 0 and int(i) < 60 and count == 1:
                    count += 1
                else:
                    print(f"YOUR TIME HAS AN ERROR NOT RIGHT VALUE:{str(user_time_)}\nPlease try again")
                    break
            if count == 2:
                print(f"Your time is {user_time_}")
                time_representation(user_time_)
                break
            elif count == 1:
                print(f"YOUR TIME HAS MISSING VALUES:  H = {str(user_time_)}:M = NONE \nPlease try again")
        break
    elif user_yes_no == "n".lower():
        time_representation(None)
        break
    print("ERROR\nPlease try again")