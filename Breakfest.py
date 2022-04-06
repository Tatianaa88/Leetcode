import time
import random


fridge = {
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
plate = {}

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


def check_availability(fridge, person_quantity):
    breakfest_items = {}
    if 'frozen fish' in fridge.keys() and fridge['frozen fish'] >= portions['frozen fish'] * person_quantity:
        breakfest_items['frozen fish'] = fridge['frozen fish']
    if 'smoked fish' in fridge.keys() and fridge['smoked fish'] >= portions['smoked fish'] * person_quantity:
        breakfest_items['smoked fish'] = fridge['smoked fish']
    if 'avokado' in fridge.keys() and fridge['avokado'] >= portions['avokado'] * person_quantity:
        breakfest_items['avokado'] = fridge['avokado']
    if 'dill' in fridge.keys() and fridge['dill'] >= portions['dill'] * person_quantity:
        breakfest_items['dill'] = fridge['dill']
    if 'parsley' in fridge.keys() and fridge['parsley'] >= portions['parsley'] * person_quantity:
        breakfest_items['parsley'] = fridge['parsley']
    if 'egg' in fridge.keys() and fridge['egg'] >= portions['egg'] * person_quantity:
        breakfest_items['egg'] = fridge['egg']
    if 'salad mix' in fridge.keys() and fridge['salad mix'] >= portions['salad mix'] * person_quantity:
        breakfest_items['salad mix'] = fridge['salad mix']
    return breakfest_items


def breakfest_types(person_quantity):
    breakfest_options = []
    breakfest_products = check_availability(fridge, person_quantity)
    if 'frozen fish' and 'avokado' in breakfest_products.keys() or ('salad mix' or ('dill' and 'pasley')) in breakfest_products.keys():
        breakfest_options.append('make_steam_fish')
        breakfest_options.append('make_fried_fish')
    if 'smoked fish' in breakfest_products.keys() and ('make_steam_fish' or 'make_fried_fish') in breakfest_options and ('smetana' or 'coconut milk') in breakfest_products and grecha_prepared():
        breakfest_options.append('smoked fish')
        breakfest_options.append('make_waffles')
    return breakfest_options


def select_breakfest(person_quantity):
    return breakfest_types(person_quantity)[0]


def make_breakfest(person_quantity):
    breakfest_option = select_breakfest(person_quantity)
    print(breakfest_option)

def make_steam_fish(person_quantity):
    print(f'Put {person_quantity} portion/portions of fish into the pot.')
    for i in range(1,41):
        # if i < 41:
        #     print(i)
        #     time.sleep(0.5)
        if i == 40:
            print(f'Fish is ready. Add {person_quantity} portion/portions of steam fish to the plate.')
            update_plate(person_quantity, 'fish', portions['frozen fish'])
    avokado_and_salad(person_quantity)
    if plate['avokado']:
        pass
    if fridge['egg']:
        make_eggs(person_quantity)


def make_fried_fish(person_quantity):
    print(f'Put {person_quantity} portion/portions of fish on the pan.')
    for i in range(1, 16):
        # if i < 16:
        #     print(i)#, end="\r")
        #     time.sleep(0.5)
        if i == 15:
            print(f'Fish is ready. Add {person_quantity} portion/portions of fried fish to the plate')
            update_plate(person_quantity, 'fish', portions['frozen fish'])
    avokado_and_salad(person_quantity)


def make_fish(time_stamp, person_quantity):
    my_time = 10
    if time_stamp < my_time:
        make_steam_fish(person_quantity)
    else:
        make_fried_fish(person_quantity)

make_breakfest(2)

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
