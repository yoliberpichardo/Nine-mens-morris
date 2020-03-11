
class Player:
    def __init__(self, name):
        self.name = name
        self.token_white = 9
        self.token_black = 9
        self.colorTokens = ['◉','◎']
        self.playerList = []
        self.inputOpcion = ''
        self.color_white = ''
        self.color_black = ''
    
def input_Player(play):
    play.playerList = []
    play.colorTokens =  ['◉','◎']
    checks = ['1','2']
    play.inputOpcion = input('Enter an option to play: ')
    while play.inputOpcion not in  checks:
        print('You input is invalid')
        play.inputOpcion = input('Enter an option to play: ')
    return play.inputOpcion

def creator_Player(play):
    input_Player(play)
    for valPlayer in range(int(play.inputOpcion)):
        play.playerList.append(Player(input('Enter the name of player{}: '.format(valPlayer + 1))))
    return play.playerList

def mapper_tokens(play):
    creator_Player(play)
    if len(play.playerList) == 1:
        play.playerList[0].colorTokens =  '◉'
        play.color_white = play.playerList[0].colorTokens 
        return play.color_white
    elif len(play.playerList) > 1:
        play.playerList[0].colorTokens =  '◉'
        play.color_white = play.playerList[0].colorTokens
        play.playerList[1].colorTokens = '◎'
        play.color_black = play.playerList[1].colorTokens
        return play.color_white, play.color_black, play.playerList
