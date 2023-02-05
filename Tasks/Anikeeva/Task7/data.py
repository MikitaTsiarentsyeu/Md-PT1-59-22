products = {
    "Motor oil": {
        "Premium":{"code":"116545","price":"42$"},
        "Pro":{"code":"116745","price":"43$"}
        },
    "Transmission oil": {
        "AXLE":{"code":"215152","price":"21$"},
        "Gear":{"code":"216352","price":"22$"}
        },
    "Hydraulic oil": {
        "46":{"code":"156920","price":"61$"},
        "32":{"code":"159920","price":"78$"}
        },
    "Antireeze": {
        "Coolant":{"code":"412650","price":"19$"},
        "Special":{"code":"413650","price":"22$"}
        },
    "Lubricants": {
        "Grease":{"code":"703245","price":"12$"},
        "superlix":{"code":"711245","price":"15$"}
    }}

def get_products():
    return products

def search(name):
    for main_value in products.values():
        for key in main_value.keys():
            if key == name:
                res = str(f'{key} : {main_value.get(name).get("price")}')
                return res