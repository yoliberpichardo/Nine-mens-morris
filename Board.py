from pieces import Piece
piece = Piece()
class Board:
    def __init__(self):
        self.board = []
        self.piece_black = piece.quant_piece()
        self.piece_white = piece.quant_piece()
        self.view_board = ''
        self.coordinate = "     0    1     2      3      4    5    6"

    
    def table(self):

        self.board = [[ [' '],'-------------',[' '],'------------',[' '] ],
                                            
                     ['  |  ', [' '],'--------', [' '],'-------',[' '],'  | '],
                            
                     ['  |    |   ',[' '],'--',[' '],'--',[' '],'  |    |   '],

                     [[' '],'',[' '],' ',[' '], '         ',[' '],'',[' '],'',[' ']],

                     ['  |    |   ',[' '],'--',[' '],'--',[' '],'  |    |     '],                       

                     ['  |  ',[' '],'--------', [' '],'-------',[' '],'  | '],

                    [ '',[' '],'-------------',[' '],'------------',[' '] ]     ] 


    
    def view(self):
        cont = 0
        for element in self.board:
            self.view_board += '\n'
            self.view_board += str(cont) + '  '
            cont += 1
            for row in element:
                self.view_board += str(row)
        self.view_board += '\n'
        self.view_board += self.coordinate
        return self.view_board

    def  move_piece(self):
        for row in self.board:
            for box in row:
                if isinstance(box,list):
                    box.pop()
                    box += 
                elif isinstance(box,str):
                    box = box
                else:
                    print('nose puede mover aqui ya hay una piesa')
        return self.board


 


table_p = Board()
table_p.table()
table_p.move_piece()
print(table_p.view())
player1 = Piece('●')
player2 = Piece('O')
