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



