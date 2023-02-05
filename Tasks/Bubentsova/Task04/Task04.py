# Task4: Split text (from text.txt) by the provided number of string characters and write to the new file

while True:
    line_symbols_number = input("Please enter the number of string characters (min number is 36) to split your text:\n")
    
    # Validation 1: The entered value is numeric
    if line_symbols_number.isdigit():
        print("Validation 1 passed")
    else:
        print("The entered value is not numeric.")
        continue

    # Validation 2: Number of the provided string characters is correct
    line_symbols_number_int = int(line_symbols_number)
    if line_symbols_number_int > 35:
        print("Validation 2 passed")
    else:
        print("The entered number is not correct. Minimum number of string characters is 36.")
        continue
    break

# Create function to split the text
def split(text, max_value):
    text_new = ''
    c = 0
    for i in text.split():
        c += len(i)
        if c + 2 > max_value:
            text_new += '\n'
            c = len(i)
        elif text_new != '':
            text_new += ' '
            c += 1
        text_new += i
    return text_new

# Define name of the new file
initial_file_name = "text.txt"
new_file_name = initial_file_name.split('.')
new_file_name[0] += "_formatted"
new_file_name = '.'.join(new_file_name)

# Read the text by using function
with open(initial_file_name, 'r') as initial_file:
    text_to_handle = initial_file.read()
    text_formatted = (split(text_to_handle, line_symbols_number_int))

text_formatted_list = list(text_formatted.split('\n'))

# Add spaces if required to the new text
for (index, item) in enumerate(text_formatted_list):
    item = item.replace('вЂњ', '"')
    item = item.replace('вЂќ', '"')
    item = item.replace('вЂ™', "'")
    item_len = len(item)
    value = line_symbols_number_int - item_len
    spaces_count = item.count(" ")
    if spaces_count == 0:
        item_new = item
    else:
        if item_len < line_symbols_number_int:
            if value <= spaces_count:
                item_new = item.replace(" ", "  ", value - 1)
            else:
                value > spaces_count
                spaces_add = value//spaces_count
                spaces_add_str = str(" " * spaces_add)
                item_new = item.replace(" ", " " + spaces_add_str, spaces_count - 1)
                item_new_len = len(item_new)
                if item_new_len < line_symbols_number_int:
                    value = line_symbols_number_int - item_new_len
                    item_new = item_new.replace(" ", "  ", value - 1)
        else:
            item_new = item
        text_formatted_list[index] = item_new

# Create text from the formatted list
text_formatted_new = ('\n').join(text_formatted_list)

# Write new text to the new file
chunk = 20
with open(new_file_name, 'w') as new_file:
    new_file.write(text_formatted_new)

# Notify user about the new file which contains splitted text
print(f"Thank you.\nInitial text was splitted on the strings by the provided number of the string characters.\nNew formatted text was written to the {new_file_name} file.")