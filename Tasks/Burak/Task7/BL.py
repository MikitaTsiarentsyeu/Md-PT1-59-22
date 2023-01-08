import Data


def addcarad(mark, model, year, engine_displacement, fuel_type, mileage, gear, location, price):
    options = {'Mark': mark, 'Model': model, 'F.r. year': year, 'Engine displacement': engine_displacement,
               'Fuel type': fuel_type, 'Mileage': mileage, 'Gear': gear, 'Location': location, 'Price': price}
    Data.addcarad(options)
    return 'Everything is fine, your ad has been submitted'

def watchallcars():
        names = Data.search_ad()
        res = []
        list_cont = []
        if len(names) > 0:
            for row in names:
                for val in row.values():
                    list_cont.append(val)
                res.append(', '.join(list_cont))
                list_cont = []
        return '\n'.join(res)

def remove(request):
        res = Data.search_ad()
        list = []
        flag = False
        for i in res:
            if i['Mark'] == request or i['Model'] == request or i['F.r. year'] == request or \
                    i['Engine displacement'] == request or i['Fuel type'] == request or i['Mileage'] == request or\
                    i['Gear'] == request or i['Location'] == request or i['Price'] == request:
                flag = True
            else:
                list.append(i)
        if flag:
            Data.remove_ad(list)
            return "The ad is removed!"
        else:
            return ''

def search(request):
        content = Data.search_ad()
        res = []
        for i in content:
            if i['Mark'] == request or i['Model'] == request or i['F.r. year'] == request or \
                    i['Engine displacement'] == request or i['Fuel type'] == request or i['Mileage'] == request or \
                    i['Gear'] == request or i['Location'] == request or i['Location'] == request or i['Price'] == request:
                for j in i.values():
                    res.append(j)
                return ' '.join(res)
        return 'Nothing was found'


