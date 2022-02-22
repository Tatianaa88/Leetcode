import time
import random


fridge = {'frozen fish': 5, 'avokado': 3, 'smoked fish': 1, 'parsley': 10, 'dill': 10, 'ready meat meals': 1, 'eggs': 10, 'liver': 2, 'salad mix': 4, 'smetana': 10}
my_time = 10
plate = {}

parsley_portion = 1
dill_portion = 1
egg_portion = 1
avokado_portion = 0.5
salad_mix_portion = 2
fish_portion = 1
waffles_portion = 3
smetana_portion = 0.5
smoked_fish_portion = 0.5
min_saladmix_quantity = 4
max_saladmix_quantity = 15


def make_eggs(person_quantity):
    for i in range(1, 16):
        # if i < 16:
        #     print(i)
        #     time.sleep(0.5)
        if i == 15:
            print('Eggs are ready')
            plate['egg'] = egg_portion
            fridge['eggs'] -= egg_portion * person_quantity


def avokado_and_salad(person_quantity):
    if fridge['avokado'] >= avokado_portion * 2:
        plate['avokado'] = avokado_portion
        fridge['avokado'] -= avokado_portion * person_quantity
        if min_saladmix_quantity <= fridge['salad mix'] <= max_saladmix_quantity:
            plate['salad mix'] = salad_mix_portion
            fridge['salad mix'] -= salad_mix_portion * person_quantity
    else:
        if min_saladmix_quantity <= fridge['salad mix'] <= max_saladmix_quantity:
            plate['salad mix'] = salad_mix_portion
            fridge['salad mix'] -= salad_mix_portion * person_quantity
        else:
            plate['parsley'] = parsley_portion
            plate['dill'] = dill_portion
            fridge['parsley'] -= parsley_portion * person_quantity
            fridge['dill'] -= dill_portion * person_quantity
        plate['parsley'] = parsley_portion
        plate['dill'] = dill_portion
        fridge['parsley'] -= parsley_portion * person_quantity
        fridge['dill'] -= dill_portion * person_quantity


def make_steam_fish(person_quantity):
    for i in range(1,41):
        # if i < 41:
        #     print(i)
        #     time.sleep(0.5)
        if i == 40:
            print('Fish is ready')
            plate['fish'] = fish_portion
            fridge['frozen fish'] -= fish_portion * person_quantity
    avokado_and_salad(person_quantity)
    if plate['avokado']:
        pass
    if fridge['eggs']:
        make_eggs(person_quantity)


def make_fried_fish(person_quantity):
    for i in range(1, 16):
        # if i < 16:
        #     print(i)#, end="\r")
        #     time.sleep(0.5)
        if i == 15:
            print('Fish is ready.')
            plate['fish'] = fish_portion
            fridge['frozen fish'] -= fish_portion * person_quantity
    avokado_and_salad(person_quantity)


def make_fish(time_stamp, person_quantity):
    if time_stamp < my_time:
        make_steam_fish(person_quantity)
    else:
        make_fried_fish(person_quantity)


def grecha_prepared():
    # return random.getrandbits(1)
    return True # change to False for testing without grecha


def make_waffles(ingredient):
    for i in range(1, 21):
        # if i < 21:
        #     print(i)#, end="\r")
        #     time.sleep(0.5)
        if i == 20:
            print('Waffles are ready.')
            plate[f'waffles with {ingredient}'] = waffles_portion
            fridge['smetana'] -= smetana_portion


def dish_selection():
    option = random.randint(1, 2)
    if option == 1:
        if 'frozen fish' in fridge and fridge['frozen fish'] >= fish_portion * 2:
            make_fish(9, 2)
    if option == 2:
        if 'smoked fish' in fridge and fridge['smoked fish'] >= smoked_fish_portion * 2:
            plate['smoked fish'] = smoked_fish_portion
            fridge['smoked fish'] -= smoked_fish_portion
            if grecha_prepared():
                if fridge['smetana'] >= smetana_portion:
                    make_waffles('smetana')
                    if fridge['avokado'] >= avokado_portion * 2:
                        plate['avokado'] = avokado_portion
                else:
                    make_waffles('coconut milk')
                    if fridge['avokado'] >= avokado_portion * 2:
                        plate['avokado'] = avokado_portion
            avokado_and_salad(2)


dish_selection()

print(f"Plate 1: {plate}")
print(f"Plate 2: {plate}")
print(f"Fridge: {fridge}")
