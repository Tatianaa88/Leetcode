import time
import random


products = {
    'frozen fish': 2,
    'avokado': 0,
    'smoked fish': 1,
    'parsley': 10,
    'dill': 10,
    'ready meat meals': 1,
    'egg': 10,
    'liver': 2,
    'salad mix': 4,
    'smetana': 10
}
my_time = 10


portions = {
    'parsley': 1,
    'dill': 1,
    'egg': 1,
    'avokado': 0.5,
    'salad mix': 2,
    'frozen fish': 1,
    'waffles': 3,
    'smetana': 0.5,
    'smoked fish': 0.5
}


# Breakfest options
steam_fried_fish = {
    'frozen fish': 1,
    'avokado': 0.5,
    'salad mix': 1
}

smoked_fish = {
    'smoked fish': 1,
    'grecha': 150,
    'smetana': 0.5,
    'avokado': 0.5

}

plate = {}
# breakfast_type = random.choice([steam_fried_fish, smoked_fish])
breakfast = steam_fried_fish


def check_availability(person_quantity, breakfast_type):
    for product, amount in breakfast_type.items():
        if product in products.keys() and products[product] >= portions[product] * person_quantity:
            breakfast_items = breakfast_type
        if (product == 'salad mix' or product == 'avokado') and products[product] < portions[product] * person_quantity:
            print('avokado test')
            breakfast_items.pop(product)
            breakfast_items['dill'] = 1
            breakfast_items['parsley'] = 1
            return breakfast_items


def make_breakfest(person_quantity, breakfest_type):
    breakfest_products = check_availability(person_quantity, breakfest_type)
    if 'frozen fish' in breakfest_products.keys():
        make_steam_fish(person_quantity, breakfest_products)
    # may be fried fish

def products_plate_update(product, person_quantity):
    plate[product] = portions[product]
    products[product] -= portions[product] * person_quantity

def make_steam_fish(person_quantity, fish_recipe):
    print('Make steam fish.')
    print(f'Put {person_quantity} portion/portions of fish into the pot.')
    for i in range(1,41):
        # if i < 41:
        #     print(i)
        #     time.sleep(0.5)
        if i == 40:
            print(f'Fish is ready. Add {person_quantity} portion/portions of steam fish to the plate.')
            for product in fish_recipe.keys():
                products_plate_update(product, person_quantity)

print(f'Products before: {products}')
make_breakfest(2, breakfast)
print(f'Plate: {plate}')
print(f'Products after: {products}')

    # if fridge['egg']:
    #     make_eggs(person_quantity)

#
# def make_fried_fish(person_quantity):
#     print(f'Put {person_quantity} portion/portions of fish on the pan.')
#     for i in range(1, 16):
#         # if i < 16:
#         #     print(i)#, end="\r")
#         #     time.sleep(0.5)
#         if i == 15:
#             print(f'Fish is ready. Add {person_quantity} portion/portions of fried fish to the plate')
#             update_plate(person_quantity, 'fish', portions['frozen fish'])
#     avokado_and_salad(person_quantity)
#
#
# def make_fish(time_stamp, person_quantity):
#     my_time = 10
#     if time_stamp < my_time:
#         make_steam_fish(person_quantity)
#     else:
#         make_fried_fish(person_quantity)
#
# make_breakfest(2)

# def check_update_availability(person_quantity, product, product_portion):
#     if product in fridge.keys() and fridge[product] >= product_portion * person_quantity:
#         fridge[product] -= product_portion * person_quantity
#         return True
#     else:
#         return False
#
#
# def update_plate(person_quantity, product, product_portion):
#     # print(f"Put {person_quantity} {product}/s into the pot and boil them.")
#     plate[product] = product_portion
#
#
# def make_eggs(person_quantity):
#     print(f'Put {person_quantity} egg/eggs into the pot and boil them.')
#     check_update_availability(person_quantity, 'egg', portions['egg'])
#     for i in range(1, 16):
#         # if i < 16:
#         #     print(i)
#         #     time.sleep(0.5)
#         if i == 15:
#             print("Egg/eggs is/are ready. Put it/them to the plate.")
#             update_plate(person_quantity, 'egg', portions['egg'])
#
#
# def avokado_and_salad(person_quantity):
#     if check_update_availability(person_quantity, 'avokado', portions['avokado']) and check_update_availability(person_quantity, 'salad mix', portions['salad mix']):
#         update_plate(person_quantity, 'avokado', portions['avokado'])
#         update_plate(person_quantity, 'salad mix', portions['salad mix'])
#     else:
#         check_update_availability(person_quantity, 'parsley',portions['parsley'])
#         check_update_availability(person_quantity, 'dill',portions['dill'])
#         update_plate(person_quantity, 'parsley', portions['parsley'])
#         update_plate(person_quantity, 'dill', portions['dill'])
#     if check_update_availability(person_quantity, 'avokado', portions['avokado']) and not check_update_availability(person_quantity, 'salad mix', portions['salad mix']):
#         update_plate(person_quantity, 'avokado', portions['avokado'])
#         update_plate(person_quantity, 'parsley', portions['parsley'])
#         update_plate(person_quantity, 'dill', portions['dill'])
#
#
# def make_steam_fish(person_quantity):
#     print(f'Put {person_quantity} portion/portions of fish into the pot.')
#     for i in range(1,41):
#         # if i < 41:
#         #     print(i)
#         #     time.sleep(0.5)
#         if i == 40:
#             print(f'Fish is ready. Add {person_quantity} portion/portions of steam fish to the plate.')
#             update_plate(person_quantity, 'fish', portions['frozen fish'])
#     avokado_and_salad(person_quantity)
#     if plate['avokado']:
#         pass
#     if fridge['egg']:
#         make_eggs(person_quantity)
#
#
# def make_fried_fish(person_quantity):
#     print(f'Put {person_quantity} portion/portions of fish on the pan.')
#     for i in range(1, 16):
#         # if i < 16:
#         #     print(i)#, end="\r")
#         #     time.sleep(0.5)
#         if i == 15:
#             print(f'Fish is ready. Add {person_quantity} portion/portions of fried fish to the plate')
#             update_plate(person_quantity, 'fish', portions['frozen fish'])
#     avokado_and_salad(person_quantity)
#
#
# def make_fish(time_stamp, person_quantity):
#     my_time = 10
#     if time_stamp < my_time:
#         make_steam_fish(person_quantity)
#     else:
#         make_fried_fish(person_quantity)
#
#
# def grecha_prepared():
#     # return random.getrandbits(1)
#     return True # change to False for testing without grecha
#
#
# def make_waffles(ingredient, person_quantity):
#     for i in range(1, 21):
#         # if i < 21:
#         #     print(i)#, end="\r")
#         #     time.sleep(0.5)
#         if i == 20:
#             print(f'Waffles are ready. Add waffles with {ingredient} to the plate')
#             update_plate(person_quantity, f'waffles with {ingredient}', portions['avokado'])
#
#
# def dish_selection(person_quantity): # pass amount of people
#     # option = 1
#     option = random.randint(1, 2)
#     if option == 1:
#         if check_update_availability(person_quantity, 'frozen fish', portions['frozen fish']):
#             print(f"Take {person_quantity} portion/portions of frozen fish from the fridge.")
#             make_fish(9, person_quantity)
#     if option == 2:
#         if check_update_availability(person_quantity, 'smoked fish', portions['smoked fish'] ):
#             print(f"Take {person_quantity} portion/portions of smoked fish from the fridge.")
#             print(f"Put {person_quantity} portion/portions of smoked fish from the fridge.")
#             update_plate(person_quantity, 'smoked fish', portions['smoked fish'])
#             if grecha_prepared():
#                 if check_update_availability(person_quantity, 'avokado', portions['avokado'] ):
#                     update_plate(person_quantity, 'avokado', portions['avokado'])
#                 if check_update_availability(person_quantity, 'smetana', portions['smetana'] ):
#                     make_waffles('smetana', person_quantity)
#                 else:
#                     make_waffles('coconut milk', person_quantity)
#             avokado_and_salad(person_quantity) #replace with amount of people
#
#
# # dish_selection(2)
#
#
# #
# # print(f"Plate 1: {plate}")
# # print(f"Plate 2: {plate}")
# # print(f"Fridge: {fridge}")
#
