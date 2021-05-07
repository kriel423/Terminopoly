import random
from wethinkcode_GroupProject_aadkriel020 import players

totalPoints = 0


def die_roll():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print('returned: ' + str(die1 + die2))


# check the number of players
# when the dice is rolled, ensure that the first player is active
# add the number to the players position
# check if the position cooincides with an item in the list
# when the item cooincides with the list, the method applicable to that card needs to be
# played
# once the action has been executed, move to the next player and repeat

# create only two players - multiple players would increase complexity of logic required

# number_of_players = players.get_num_players()
# i = 0

# question = input('Would you like to roll the die? y | n')
# if question == 'y':
#     die_roll()
#     while i < len(number_of_players):
#         players.my_players[i].player_position =+ die_roll()
#         if(players.my_players[i].player_position == )
#         i += 1
#
#
#         if players.number_of_players_in_game()
#         die_roll()
#         print('Move'+players.my_players())
#         players.my_players.
#         break
#
#     if question == 'n':
#         followUp = input('Skip a turn? y | n')
#         if followUp == 'y':
#             print('Skipped a turn')
