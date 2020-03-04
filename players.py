from pieces import Piece

class Player:
    def __init__(self,nombre):
        self.nombre = nombre
        self.turn = 0
        self.tokens = None
        # self.characte = ['◉',' ◎']
        

    def player1(self,nombre):
        self.nombre = input('player1 enter you name: ') 
        self.turn = 1
        self.tokens = Piece('◉')
        print(self.tokens.quant_piece())
        return self.tokens.symbol * 1

    def player2(self,nombre):
        self.nombre = input('player2 enter you name: ') 
        self.turn = 2
        self.tokens = Piece('◎')
        print(self.tokens.quant_piece())
        return self.tokens.symbol * 1

        
    
        


     
    