from itertools import cycle
from wethinkcode_GroupProject_aadkriel020 import properties
from wethinkcode_GroupProject_aadkriel020 import players
from wethinkcode_GroupProject_aadkriel020 import dieRoll
import random

# -----------------------Playable Blocks---------------------------

playableBlocks = ['Begin', 'OOP-sy B&B', 'Python Hotel', 'Jail', 'CSS Heights', 'Chance',
                  'JS Inn', 'Community Chest', 'Free Parking', 'Memory Space', 'RAM House',
                  'Go straight to Jail', 'Cache De Cookie', 'Community Chest', 'ROM-ance Inn',
                  'Chance']

# ---------------------------------------------------------------------

# -----------------------Street Blocks---------------------------------

javaStreet = ['Python hotel', 'OOP-sy B&B']
hTML_DOM_Lane = ['CSS Heights', 'JS Inn']
Assembly = ['Memory Space', 'RAM house']
CPUCity = ['Cache de Cookie', 'ROM-ance Inn']

# ---------------------------------------------------------------------

# -----------------------Chance & Com. Chest---------------------------

community_chest = {'Advance': 200, 'Bank Error': 100, 'Doctor': -50, 'Hospital': -100}

chance = {'Get Out of Jail': 21, 'Loan': 150, 'Bank Pay': -50, 'House': -25}

# ---------------------------------------------------------------------

# -----------------------Properties------------------------------------

oop_sy_bnb = properties.Properties('OOP-sy B&B', 45, 1)
python_hotel = properties.Properties('Python Hotel', 35, 1)
css_heights = properties.Properties('CSS Heights', 60, 2)
js_inn = properties.Properties('JS Inn', 60, 2)
memory_space = properties.Properties('Memory Space', 150, 8)
ram_house = properties.Properties('RAM House', 175, 10)
cache_de_cookie = properties.Properties('Cache de Cookie', 80, 3)
rom_ance_inn = properties.Properties('ROM-ance Inn', 90, 3)

# ---------------------------------------------------------------------

# -----------------------Create Players--------------------------------

player1_name = input('Player 1 name: ')
player2_name = input('Player 2 name: ')

player1 = players.Players(player1_name, 500, '')
player2 = players.Players(player2_name, 500, '')


def instantiate_players():
    player = ' '
    while player != player1.get_name() or player != player2.get_name():
        if player == player1.get_name():
            dice_roll = dieRoll.die_roll()
            ticker = 0
            wtc_currency = 0
            purchase_or_rent = ''
            # position = ''
            current_item = ''
            locations = cycle(playableBlocks)

            while ticker != dice_roll:
                next(locations)
                current_item = next(locations)
                ticker += 1
                if ticker == dice_roll:
                    player1.set_player_position(playableBlocks)
                    break

            if player1.get_position() == oop_sy_bnb.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player1.set_money(player1.get_money() - oop_sy_bnb.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player1.set_money(player1.get_money() - oop_sy_bnb.get_buy_rate())
            elif player1.get_position() == python_hotel.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player1.set_money(player1.get_money() - python_hotel.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player1.set_money(player1.get_money() - python_hotel.get_buy_rate())
            elif player1.get_position() == css_heights.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player1.set_money(player1.get_money() - css_heights.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player1.set_money(player1.get_money() - css_heights.get_buy_rate())
            elif player1.get_position() == js_inn.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player1.set_money(player1.get_money() - js_inn.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player1.set_money(player1.get_money() - js_inn.get_buy_rate())
            elif player1.get_position() == memory_space.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player1.set_money(player1.get_money() - memory_space.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player1.set_money(player1.get_money() - memory_space.get_buy_rate())
            elif player1.get_position() == ram_house.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player1.set_money(player1.get_money() - ram_house.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player1.set_money(player1.get_money() - ram_house.get_buy_rate())
            elif player1.get_position() == cache_de_cookie.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player1.set_money(player1.get_money() - cache_de_cookie.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player1.set_money(player1.get_money() - cache_de_cookie.get_buy_rate())
            elif player1.get_position() == rom_ance_inn.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player1.set_money(player1.get_money() - rom_ance_inn.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player1.set_money(player1.get_money() - rom_ance_inn.get_buy_rate())
            elif player1.get_position() == 'Community Chest':
                wtc_currency = random.choice(list(community_chest.values()))
                player1.set_money(player1.get_money() + wtc_currency)
            elif player1.get_position() == 'Chance':
                wtc_currency = random.choice(list(chance.values()))
                if wtc_currency == 21:
                    player1.set_player_position('Jail')
                elif wtc_currency == 150:
                    player1.set_money(player1.get_money() + wtc_currency)
                elif wtc_currency == -50:
                    player1.set_money(player1.get_money() + wtc_currency)
                elif wtc_currency == -25:
                    player1.set_money(player1.get_money() + wtc_currency)
                else:
                    break
            elif player1.get_position() == 'Free Parking':
                player1.set_player_position('Free Parking')
            else:
                player1.set_player_position('Begin')

        elif player == player2.get_name():
            dice_roll = dieRoll.die_roll()
            ticker = 0
            # position = ''
            current_item = ''
            locations = cycle(playableBlocks)

            while ticker != dice_roll:
                next(locations)
                current_item = next(locations)
                ticker += 1
                if ticker == dice_roll:
                    player2.set_player_position(playableBlocks)
                    break

            if player2.get_position() == oop_sy_bnb.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player2.set_money(player2.get_money() - oop_sy_bnb.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player2.set_money(player2.get_money() - oop_sy_bnb.get_buy_rate())
            elif player2.get_position() == python_hotel.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player2.set_money(player2.get_money() - python_hotel.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player2.set_money(player2.get_money() - python_hotel.get_buy_rate())
            elif player2.get_position() == css_heights.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player2.set_money(player2.get_money() - css_heights.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player2.set_money(player2.get_money() - css_heights.get_buy_rate())
            elif player2.get_position() == js_inn.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player2.set_money(player2.get_money() - js_inn.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player2.set_money(player2.get_money() - js_inn.get_buy_rate())
            elif player2.get_position() == memory_space.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player2.set_money(player2.get_money() - memory_space.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player2.set_money(player2.get_money() - memory_space.get_buy_rate())
            elif player2.get_position() == ram_house.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player2.set_money(player2.get_money() - ram_house.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player2.set_money(player2.get_money() - ram_house.get_buy_rate())
            elif player2.get_position() == cache_de_cookie.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player2.set_money(player2.get_money() - cache_de_cookie.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player2.set_money(player2.get_money() - cache_de_cookie.get_buy_rate())
            elif player2.get_position() == rom_ance_inn.get_name():
                purchase_or_rent = input('Rent or Purchase? R | P').lower()
                if purchase_or_rent == 'r':
                    player2.set_money(player2.get_money() - rom_ance_inn.get_rent_rate())
                elif purchase_or_rent == 'p':
                    player2.set_money(player2.get_money() - rom_ance_inn.get_buy_rate())
            elif player2.get_position() == 'Community Chest':
                wtc_currency = random.choice(list(community_chest.values()))
                player2.set_money(player2.get_money() + wtc_currency)
            elif player2.get_position() == 'Chance':
                wtc_currency = random.choice(list(chance.values()))
                if wtc_currency == 21:
                    player2.set_player_position('Jail')
                elif wtc_currency == 150:
                    player2.set_money(player2.get_money() + wtc_currency)
                elif wtc_currency == -50:
                    player2.set_money(player2.get_money() + wtc_currency)
                elif wtc_currency == -25:
                    player2.set_money(player2.get_money() + wtc_currency)
                else:
                    break
            elif player2.get_position() == 'Free Parking':
                player2.set_player_position('Free Parking')
            else:
                player2.set_player_position('Begin')


# ---------------------------------------------------------------------

# Lets start playing the game!
# to get to the first position, roll the dice and subtract 1

instantiate_players()


# -----------------------Player Status--------------------------------

def check_player_status():
    print(
        'Player 1:\nName: ' + player1.get_name() + '\nMoney: ' + player1.get_money()
        + '\nPosition: ' + player1.get_position())
    print(
        'Player 2:\nName: ' + player2.get_name() + '\nMoney: ' + player2.get_money()
        + '\nPosition: ' + player2.get_position())


# ---------------------------------------------------------------------

check_player_status()
