class Player:
    def __init__(self, name):
        self.name = name
        self.token = 9
        self.colorTokens = ''

playerList = []
def input_Player():
    checks = ['1','2']
    inputOpcion = input('Enter an option to play: ') 
    while inputOpcion not in  checks:
        print('You input is invalid')
        inputOpcion = input('Enter an option to play: ')
    return int(inputOpcion)

def creator_Player():
    verified_entry = input_Player()
    for valPlayer in range(verified_entry):
        playerList.append(Player(input('Enter the name of player{}: '.format(valPlayer + 1))))
    return playerList

def mapper_tokens():
    creator_Player()
    if len(playerList) == 1:
        playerList[0].colorTokens =  '◉'
        return playerList[0].colorTokens
    elif len(playerList) > 1:
        playerList[0].colorTokens =  '◉'
        playerList[1].colorTokens = '◎'
        return playerList[1].colorTokens, playerList[0].colorTokens
