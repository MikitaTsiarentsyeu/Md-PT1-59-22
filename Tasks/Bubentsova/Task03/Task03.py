# Task3> Display time value in the hh:mm format based on the selected by user option: 1. time entered via console, 2. current time

import sys
from datetime import datetime
from hours_dictionary import hours_dictionary
from hours2_dictionary import hours2_dictionary
from minutes_dictionary import minutes_dictionary

while True:
    option = input("Hello, would you like to type the time value by yourself (yes/no)?\n")
    if option == "yes":
        time_value_string = input("Please enter the time value in the following format: hh:mm\n")

        # Validation 1: The entered time value contains ":" symbol
        if ":" in time_value_string:
            print("Validation 1 passed")
        else:
            print("Format of the entered time value is not correct, ':' is missing.")
            continue

        # Validation 2: The entered time value is numeric
        time_value_list = time_value_string.split(":")
        hours = time_value_list[0]
        minutes = time_value_list[1]
        if hours.isdigit() and minutes.isdigit():
            print("Validation 2 passed")
        else:
            print("The entered time value is not numeric. Please revrite your time value.")
            continue

        # Validation 3: The entered time value contains two symbols for hours and minutes
        hours_len = len(hours)
        minutes_len = len(minutes)
        if hours_len == 2 and minutes_len == 2:
            print("Validation 3 passed")
        else:
            print("Format of the entered time value is not correct. Some digit(s) is missing or redundant. Please rewrite your time value.")
            continue

        # Validation 4: Maximum value for hours is correct
        hours_int = int(hours)
        if hours_int <= 23:
            print("Validation 4 passed")
        else:
            print("The entered time value is not correct. Maximum value for hours should be less or the same as 23.")
            continue

        # Validation 5: Maximum value for minutes is correct
        minutes_int = int(minutes)
        if minutes_int <= 59:
            print("Validation 5 passed")
        else:
            print("The entered time value is not correct. Maximum value for minutes should be less or the same as 59.")
            continue

        # Determine entered time value wording
        if time_value_string == "00:00" or time_value_string == "12:00":
            time_value = hours2_dictionary[hours_int]
        elif hours_int in range(0, 6):
            if minutes_int == 00:
                hours_wording = hours2_dictionary[hours_int]
                time_value = hours_wording + " ночи"
            elif minutes_int >=45:
                hours_int += 1
                hours_wording = hours2_dictionary[hours_int]
                minutes_wording = minutes_dictionary[minutes_int]
                time_value = ' '.join([minutes_wording,hours_wording]) + " ночи"
            else:
                hours_int += 1
                hours_wording = hours_dictionary[hours_int]
                minutes_wording = minutes_dictionary[minutes_int]
                time_value = ' '.join([minutes_wording,hours_wording]) + " ночи"
        elif hours_int in range(6, 12):
            if minutes_int == 00:
                hours_wording = hours2_dictionary[hours_int]
                time_value = hours_wording + " утра"
            elif minutes_int >=45:
                hours_int += 1
                hours_wording = hours2_dictionary[hours_int]
                minutes_wording = minutes_dictionary[minutes_int]
                time_value = ' '.join([minutes_wording,hours_wording]) + " утра"
            else:
                hours_int += 1
                hours_wording = hours_dictionary[hours_int]
                minutes_wording = minutes_dictionary[minutes_int]
                time_value = ' '.join([minutes_wording,hours_wording])
        elif hours_int in range(12, 18):
            if minutes_int == 00:
                hours_wording = hours2_dictionary[hours_int]
                time_value = hours_wording + " дня"
            elif minutes_int >=45:
                hours_int += 1
                hours_wording = hours2_dictionary[hours_int]
                minutes_wording = minutes_dictionary[minutes_int]
                time_value = ' '.join([minutes_wording,hours_wording]) + " дня"
            else:
                hours_int += 1
                hours_wording = hours_dictionary[hours_int]
                minutes_wording = minutes_dictionary[minutes_int]
                time_value = ' '.join([minutes_wording,hours_wording])
        else:
            hours_int in range(18, 24)
            if minutes_int == 00:
                hours_wording = hours2_dictionary[hours_int]
                time_value = hours_wording + " вечера"
            elif minutes_int >=45:
                hours_int += 1
                hours_wording = hours2_dictionary[hours_int]
                minutes_wording = minutes_dictionary[minutes_int]
                if hours_int == 24:
                    time_value = minutes_wording + " полночь"
                else:
                    time_value = ' '.join([minutes_wording,hours_wording]) + " вечера"
            else:
                hours_int += 1
                hours_wording = hours_dictionary[hours_int]
                minutes_wording = minutes_dictionary[minutes_int]
                time_value = ' '.join([minutes_wording,hours_wording])

        # Display entered time value wording in Russian
        print(f"The entered time value wording in Russian:\n{hours}:{minutes} - {time_value}")
    else:
        # Display current time
        current_time = datetime.now()
        print("Current time:\n{:02}:{:02}".format(current_time.hour, current_time.minute))
        sys.exit()