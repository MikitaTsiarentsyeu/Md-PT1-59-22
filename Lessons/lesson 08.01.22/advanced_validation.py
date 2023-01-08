control_value = 20

while True:
    number = input(f"Please enter a whole number not less than {control_value}:\n")
    try:
        number = int(number)
        if number < control_value:
            raise RuntimeError(f"The number should be not less than {control_value}")
    except ValueError:
        print("Please anter a valid number")
        continue
    except RuntimeError as e:
        print(e)
        continue
    else:
        break


print("All is set, the process will start in a moment")