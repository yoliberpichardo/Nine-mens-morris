from pieces import Piece

class Player:
    def __init__(self,nombre):
        self.nombre = nombre
        self.turn = 0
        # self.characte = ['◉',' ◎']
        

    def player1(self,nombre):
        self.nombre = input('player1 enter you name: ') 
        self.turn = 1
        tokens = Piece('◉ ')
        return tokens.quant_piece()

    def player2(self,nombre):
        self.nombre = input('player2 enter you name: ') 
        self.turn = 2
        token = Piece('◎ ')
        return token.quant_piece()

        
    # def change_turn(self,turn):
        
p1 = Player('nombre')  
print(p1.player1('nombre'))
print(p1.player2(' '))

     
    