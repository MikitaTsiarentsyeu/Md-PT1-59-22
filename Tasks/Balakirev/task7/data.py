import csv
import os

head = ['Surname', 'Name', 'Number']
with open("phonebook.csv", 'w', encoding='UTF-8', newline='') as f:
    writer = csv.DictWriter(f, delimiter=',', lineterminator='\r', fieldnames=head)
    writer.writeheader()
    writer.writerow({'Surname': 'Ivanov', 'Name': 'Ivan', 'Number': '375331234567'})
    writer.writerow({'Surname': 'Sidorov', 'Name': 'Igor', 'Number': '375214234567'})


def add_contact(info):
    with open("phonebook.csv", 'a', encoding='UTF-8', newline='') as contact:
        writer = csv.DictWriter(contact, delimiter=',', fieldnames=head)
        writer.writerow(info)
    sorted_contact()


def directory_data():
    with open("phonebook.csv", 'r', encoding='UTF-8', newline='') as contact:
        reader = csv.DictReader(contact, delimiter=',')
        elem = []
        for row in reader:
            elem.append(dict(row))
        return elem


def sorted_contact():
    with open("phonebook.csv", 'r', encoding='UTF-8', newline='') as contact:
        reader = csv.DictReader(contact, delimiter=',')
        elem = []
        for row in reader:
            elem.append(dict(row))
        result = sorted(elem, key=lambda i: i['Surname'])
    remove_rename(result)


def remove_rename(res):
    with open("phonebook123.csv", 'w', encoding='UTF-8', newline='') as cont:
        writer = csv.DictWriter(cont, fieldnames=head)
        writer.writeheader()
        for x in res:
            writer.writerow(x)
    os.remove("phonebook.csv")
    os.rename("phonebook123.csv", "phonebook.csv")
