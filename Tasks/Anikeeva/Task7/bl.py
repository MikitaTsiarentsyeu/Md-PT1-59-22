import data

def get_products():
    p = data.get_products()
    return '  |  '.join(p.keys())


def get_motor_oil():
    m = data.get_products()
    motor_oil = m.get("Motor oil")
    return '\n'.join([f"{item}: {', '.join([f'{k} - {v}' for k, v in value.items()])}" for item, value in motor_oil.items()])

def get_transmission_oil():   
    t = data.get_products() 
    transmission_oil = t.get("Transmission oil")  
    return '\n'.join([f"{item}: {', '.join([f'{k} - {v}' for k, v in value.items()])}" for item, value in transmission_oil.items()])

def get_hydraulic_oil():
    h = data.get_products()
    hydraulic_oil = h.get("Hydraulic oil")  
    return '\n'.join([f"{item}: {', '.join([f'{k} - {v}' for k, v in value.items()])}" for item, value in hydraulic_oil.items()])

def get_antireeze():
    a = data.get_products()
    antireeze = a.get("Antireeze")  
    return '\n'.join([f"{item}: {', '.join([f'{k} - {v}' for k, v in value.items()])}" for item, value in antireeze.items()])

def get_lubricants():
    l = data.get_products()
    lubricants = l.get("Lubricants")  
    return '\n'.join([f"{item}: {', '.join([f'{k} - {v}' for k, v in value.items()])}" for item, value in lubricants.items()])

def get_all():
    return (f"{get_motor_oil()}\n{get_transmission_oil()}\n{get_hydraulic_oil ()}\n{get_antireeze()}\n{get_lubricants()}")


basket = []
def add_to_basket(name):
    res = data.search(name)
    basket.append(res)   
    return "\n".join(basket)

def total_amount():
    sum = 0
    for string in basket:
        for w in string.split(' '):
            if "$" in w:
                w = w[:-1]
                sum = sum + int(w)
    return f"{sum}$"