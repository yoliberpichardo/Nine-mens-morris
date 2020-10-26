from os import system
class Player:
    def __init__(self, name):
        self.name = name
        self.token = 9
        self.colorTokens = ''
        
playerList = []
#--------------------------------------------------------------METHOD FOR ENTERING NAME OF PLAYERS----------------------------------------------------------------#
def namesPlayers():
    """The next loop goes through in range of two and asks player 1 and player 2 for names."""
    for valPlayer in range(2):
        inputName = input('» Enter the name of player{}: '.format(valPlayer + 1))
        while len(inputName) > 11 or len(inputName) == 0:
            system('cls')
            print('You must enter valid names, re-enter your name!')
            inputName = input('» Enter the name of player{}: '.format(valPlayer + 1))
        if inputName == 'exit' or inputName == 'EXIT':
            system('cls')
            exit()
        else:
            playerList.append(Player(inputName.upper()))
    return playerList
#---------------------------------------------------------------METHOD ASSIGN TAB TO EACH PLAYER--------------------------------------------------------------------#
def mapper_tokens():
    """According to the length of the playerlist variable, here the token is assigned to each player."""
    namesPlayers()
    if len(playerList) == 1:
        playerList[0].colorTokens =  '◉'
        return playerList[0].colorTokens
    elif len(playerList) > 1:
        playerList[0].colorTokens = '◉'
        playerList[1].colorTokens = '◎'
        return playerList[1].colorTokens, playerList[0].colorTokens

