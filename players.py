class Player:
    def __init__(self,nombre):
        self.nombre = nombre
        self.tokens = 9
        self.colorTokens = '' 
    
    def change_turn(self):
        if self.colorTokens == '◉':
            return '◎'
        return '◉'

change = Player(' ')
def optionPlayer():
    playerList = []
    colorTokens = ['◉','◎']
    checks = '12'
    inputOpcion = input('Enter the number of players, the way to play is player vs player or player vs boot: ')
    while inputOpcion not in  checks:
        print('You input is invalid')
        inputOpcion = input('Enter the number of players, the way to play is player vs player or player vs boot: ')
    
    for valPlayer in range(int(inputOpcion)):
        playerList.append(Player(input('Enter the name of player{}: '.format(valPlayer + 1))))
    playerList[0].colorTokens, playerList[1].colorTokens  = '◉' , '◎'
    if playerList[0] == '1':
        return playerList[0].colorTokens
    else:
        return playerList[1].colorTokens
    



 
    