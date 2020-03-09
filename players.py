
class Player:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tokens = 9
        self.colorTokens = '' 
        self.turnPlayer = ''

def optionPlayer():
    playerList = []
    colorTokens =  ['◉','◎']
    checks = '12'
    inputOpcion = input('Enter the number of players, the way to play is 1--player vs boot, or 2--player vs player:  ')
    while inputOpcion not in  checks:
        print('You input is invalid')
        inputOpcion = input('Enter the number of players, the way to play is 1--player vs boot, or 2--player vs player:   ')
    
    for valPlayer in range (0, int(inputOpcion)):
        playerList.append(Player(input('Enter the name of player{}: '.format(valPlayer + 1))))
        print(colorTokens[valPlayer])
        
        if colorTokens[valPlayer] == '◎':
            result = Player('player2')
        return colorTokens[valPlayer]

    




