class Player:
    def __init__(self,nombre):
        self.nombre = nombre
        self.tokens = 9
        self.colorTokens = ['◉','◎']
        self.playerList = []
        self.inputOpcion = ''
        self.color_white = ''
        self.color_black = ''
        
play = Player('')
def input_Player():
    play.playerList = []
    play.colorTokens =  ['◉','◎']
    checks = '2'
    play.inputOpcion = input('Enter the number of players, the way to play is player vs player or player vs boot: ')
    while play.inputOpcion not in  checks:
        print('You input is invalid')
        play.inputOpcion = input('Enter the number of players, the way to play is player vs player or player vs boot: ')
    return play.inputOpcion

def creator_Player():
    if input_Player():
        for valPlayer in range(int(play.inputOpcion)):
            play.playerList.append(Player(input('Enter the name of player{}: '.format(valPlayer + 1))))
        return play.playerList
    print('no introdujo los players correctos')

def mapper_tokens():
    if  creator_Player():
        if len(play.playerList) == 1:
            play.playerList[0].colorTokens =  '◉'
            play.color_white = play.playerList[0].colorTokens 
            return play.color_white,
        elif len(play.playerList) > 1:
            play.playerList[0].colorTokens =  '◉'
            play.color_white = play.playerList[0].colorTokens
            play.playerList[1].colorTokens = '◎'
            play.color_black = play.playerList[1].colorTokens
            return play.color_white, play.color_black
    print('no existen jugadores')

print(mapper_tokens())






    
