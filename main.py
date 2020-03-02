from Board import Board
from pieces import Piece
from os import system

player1 = Piece('●')
player2 = Piece('O')
class game:
    def __init__(self,game_start):
        self.game_start = game_start
        
    
    def piece_add(self,player1,player2):
        self.game_start = input('press enter')
        while(player1 + player2 != -1):
            if player1 >= 3:
                



table_p = Board()
table_p.table()
table_p.move_piece()
print(table_p.view())
