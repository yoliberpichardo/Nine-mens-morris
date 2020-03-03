from Board import Board
from pieces import Piece
from os import system

player1 = Piece('●')
player2 = Piece('O')
board = Board()
class game:
    def __init__(self):
        self.game_start = input('press enter for start')
        
    
    def input_Piece_board(self):
        cont_turn = 1
        while self.player.quant != 0:
            if cont_turn == 1:
                board.input_coordinate(player1)
                self.player1.quant - 1
                cont_turn += 1
            elif cont_turn == 2:
                board.input_coordinate(player2)
                self.player1.quant - 1
                cont_turn -= 1
        
            



    


table_g = game()
table_p = Board()
table_p.table()
table_p.input_coordinate()
print(table_p.view())
