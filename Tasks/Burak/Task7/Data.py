import csv
import os

PATH = 'cars.csv'
options = ['Mark', 'Model', 'F.r. year', 'Engine displacement', 'Fuel type', 'Mileage', 'Gear', 'Location', 'Price']

# with open(PATH, 'w', encoding='utf-8') as w:
#     file_writer = csv.DictWriter(w,  extrasaction='ignore', delimiter = ',', lineterminator = '\r', fieldnames = options)
#     file_writer.writerow({'Mark': 'Audi', 'Model': 'A6', 'F.r. year': '2007', 'Engine displacement':'2.0',
#                      'Fuel type':'Petrol', 'Mileage':'20000', 'Gear':'Auto', 'Location':'Minsk', 'Price':'2000'})

def addcarad(opt):
    with open(PATH, 'a', encoding='UTF-8') as ad:
        writer = csv.DictWriter(ad, delimiter=',', fieldnames=options)
        writer.writerow(opt)


def search_ad():
    with open(PATH, 'r', encoding='UTF-8', newline='') as s:
        content = csv.DictReader(s)
        list = []
        for i in content:
            list.append(dict(i))
        return list

def remove_ad(request):
    with open(PATH, 'w', encoding='UTF-8', newline='') as r:
        writer = csv.DictWriter(r, fieldnames=options)
        writer.writeheader()
        for i in request:
            os.remove(request)
            writer.writerow(i)


