def split_str(string, length):
    text = string.split()
    mylist = []
    nested_list = []
    count = 0
    for i in text:
        if count+len(i)+1 <= length:
            count += len(i) + 1
            nested_list.append(i)
        else:
            if count <= length:
                space = length - count
                while space != 0:
                    if space < len(nested_list):
                        for j in range(space):
                            nested_list[j] = nested_list[j]+' '
                        space = 0
                    else:
                        for j in range(len(nested_list)):
                            nested_list[j] = nested_list[j]+' '
                        space -= len(nested_list)-1
            mylist.append(nested_list)
            nested_list = []
            nested_list.append(i)
            count = len(i)+1
    mylist.append(nested_list)
    for i in range(len(mylist)):
        mylist[i] = ' '.join(mylist[i])
    return '\n'.join(mylist)


length = int(input('Maximum number of characters per line(at least 35): \n'))
if length < 35:
    print('And you are a joker')
else:
    with open('text.txt', 'r', encoding='UTF-8') as txt:
        content = txt.readlines()
        new_text = []
        for i in range(len(content)):
            new_text.append(split_str(content[i], length))
        with open('new_text.txt', 'w+', encoding='UTF-8') as file:
            file.writelines('\n'.join(new_text))
        with open('new_text.txt', 'r', encoding='UTF-8') as new_file:
            print('You have created a new text file with the following content:')
            print(new_file.read())


