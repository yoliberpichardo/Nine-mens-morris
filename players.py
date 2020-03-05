class Player:
    def __init__(self,nombre):
        self.nombre = nombre
        self.tokens = 9
        self.colorTokens = '' 
    
def optionPlayer():
    playerList = []
    colorTokens =  ['◉','◎']
    checks = '12'
    inputOpcion = input('Enter the number of players, the way to play is player vs player or player vs boot: ')
    while inputOpcion not in  checks:
        print('You input is invalid')
        inputOpcion = input('Enter the number of players, the way to play is player vs player or player vs boot: ')
    
    for valPlayer in range(int(inputOpcion)):
        playerList.append(Player(input('Enter the name of player{}: '.format(valPlayer + 1))))
        print(colorTokens[valPlayer])
        return colorTokens[valPlayer]
    

    # def change_turn(): 

    