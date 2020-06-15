from os import system
class Player:
    def __init__(self, name):
        self.name = name
        self.token = 3
        self.colorTokens = ''

playerList = []
def namesPlayers():
    for valPlayer in range(2):
        inputName = input('Enter the name of player{}: '.format(valPlayer + 1))
        if len(inputName) == 0 or len(inputName) > 8:
            print('Your name should not exceed more than 9 letters, re-enter your name!')
            inputName = input('Enter the name of player{}: '.format(valPlayer + 1))
        playerList.append(Player(inputName))
    return playerList

def mapper_tokens():
    namesPlayers()
    if len(playerList) == 1:
        playerList[0].colorTokens =  '◉'
        return playerList[0].colorTokens
    elif len(playerList) > 1:
        playerList[0].colorTokens = '◉'
        playerList[1].colorTokens = '◎'
        return playerList[1].colorTokens, playerList[0].colorTokens

