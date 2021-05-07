class Players:
    def __init__(self, name, money, player_position):
        self._name = name
        self._money = money
        self._player_position = player_position

    def player_details(self):
        print('Member details\nName:' + self._name + '\nNet Worth: WTC' + self._money + '\nPlayer Position: '+ self._player_position)

    def get_name(self):
        return self._name

    def get_money(self):
        return self._money

    def get_position(self):
        return self._player_position

    def set_name(self, new_name):
        self._name = new_name

    def set_money(self, new_money):
        self._money = new_money

    def set_player_position(self, new_player_position):
        self._player_position = new_player_position
    #
    # def net_worth(self):
    #     self.money = 'WTC500'


# number_of_players = int(input('How many players?'))
# my_players = []
#
# i = 0
#
# while i < number_of_players:
#     name = input('Player1 name' + str(i + 1) + ' name: ').format(i)
#     money = 500
#     player_position = 0
#     my_players.append(Players(name, money, player_position))
#     i += 1
#
#
# def view_players():
#     for obj in my_players:
#         print(obj.name, obj.money, obj.player_position, sep=' | ')
#
#
# view_database = input('View Player Details? Y | N\n')
# if view_database == 'Y':
#     view_players()
#
#
# def get_num_players():
#     return len(my_players)
