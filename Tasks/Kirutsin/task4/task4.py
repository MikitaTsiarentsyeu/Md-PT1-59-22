# source
index = 0
final_string = ''
user_choise = int(input('Hello!\nPlease provide maximum number of characters per line.Input please, your value:\n'))
source = open('../../!Tasks/Task4/text.txt', 'r')
text = source.read().replace('\n', '')
format_string = ''

# formatting
for i in text:
    format_string +=i
    index = index + 1

    if index == user_choise - 1:
        index = 0

       # formating
        if format_string[0] == ' ':
            replace_point = format_string[1:].find(' ')
            result = format_string[1:replace_point + 1] + ' ' + format_string[replace_point + 1:]

            if result[-1] != ' ' and result[-1] != '-' and result[-1] != '.' and result[-1] != ',':
                result = result + '-'

            final_string += result + '\n'

        elif format_string[-1] == ' ':
            reverse = format_string[::-1]
            replace_point = reverse[1:].find(' ')
            result = reverse[1:replace_point + 1] + ' ' + reverse[replace_point + 1:]
            result = result[::-1]

            if result[-1] != ' ' and result[-1] != '-' and result[-1] != '.' and result[-1] != ',':
                result = result + '-'

            final_string += result + '\n'

        else:
            if format_string[-1] != ' ' and format_string[-1] != '-' and format_string[-1] != '.' and format_string[-1] != ',':
                format_string = format_string + '-'

            final_string += format_string + '\n'

        format_string = ''

# result text
with open("result.txt",'w') as f:
    f.write(final_string)