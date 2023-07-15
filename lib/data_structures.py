spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    new_list = []
    for i in range(len(spicy_foods)):
        name = spicy_foods[i]['name']
        new_list.append(name)
    return new_list


def get_spiciest_foods(spicy_foods):
    new_list=[elem for elem in spicy_foods if elem["heat_level"]>5]
    return new_list


def print_spicy_foods(spicy_foods):
    for i in range(len(spicy_foods)):
        heat = spicy_foods[i]["heat_level"]
        print(f'{spicy_foods[i]["name"]} ({spicy_foods[i]["cuisine"]}) | Heat Level: {heat * "🌶"}')
   

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    new_list = [elem for elem in spicy_foods if elem["cuisine"] == cuisine]
    new_dict = dict()
    for i in range(len(new_list)):
        new_dict["name"]=new_list[i]["name"]
        new_dict["cuisine"]=new_list[i]["cuisine"]
        new_dict["heat_level"]=new_list[i]["heat_level"]

    return new_dict




def print_spiciest_foods(spicy_foods):
    for i in range(len(spicy_foods)):
        heat = spicy_foods[i]["heat_level"]
        if heat >5:
            print(f'{spicy_foods[i]["name"]} ({spicy_foods[i]["cuisine"]}) | Heat Level: {heat * "🌶"}')

def get_average_heat_level(spicy_foods):
    heat = 0
    ave = 0
    for i in range(len(spicy_foods)):
        heat += spicy_foods[i]["heat_level"]
        ave = heat/len(spicy_foods)
    return ave

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
