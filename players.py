class Players:
    def __init__(self, name, money, player_position):
        self.name = name
        self.money = money
        self.player_position = player_position

    def player_details(self):
        print('Member details\nName:' + self.name + '\nNet Worth:' + self.money + '\nPlayer Position: '+self.player_position)
    #
    # def net_worth(self):
    #     self.money = 'WTC500'


number_of_players = int(input('How many players?'))
my_players = []

i = 0

while i < number_of_players:
    name = input('Player' + str(i + 1) + ' name: ').format(i)
    money = 'WTC500'
    player_position = 0
    my_players.append(Players(name, money, player_position))
    i += 1


def view_players():
    for obj in my_players:
        print(obj.name, obj.money, obj.player_position, sep=' | ')


view_database = input('View Player Details? Y | N\n')
if view_database == 'Y':
    view_players()


def get_num_players():
    return len(my_players)
