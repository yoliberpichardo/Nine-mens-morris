from os import system
class Player:
    def __init__(self, name1, name2):
        self.name_player1 = name1
        self.name_player2 = name2
        self.token = 3
        self.colorTokens = ''


# def input_Player():
#     checks = ['1','2']
#     inputOpcion = input('Enter an option to play: ') 
#     while inputOpcion not in checks:
#         system('cls')
#         print('You input is invalid')
#         inputOpcion = input('Enter an option to play: ')
#     return int(inputOpcion)

    def creator_Player(self):
        names_player = Player('name1', 'name2')
        names_player.name_player1 = input('Enter the name of player 1: ')
        names_player.name_player2 = input('Enter the name of player 2: ')
        print(names_player.name_player1)
    

playerList = []
def mapper_tokens():
    creator_Player()
    if len(playerList) == 1:
        playerList[0].colorTokens =  '◉'
        return playerList[0].colorTokens
    elif len(playerList) > 1:
        playerList[0].colorTokens =  '◉'
        playerList[1].colorTokens = '◎'
        return playerList[1].colorTokens, playerList[0].colorTokens
    

