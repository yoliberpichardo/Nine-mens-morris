from pieces import Piece
piece = Piece(input('enter one color: ') )
class Board:
    def __init__(self):
        self.board = []
        self.view_board = ''
        self.coordinate = "   a  b  c  d  e  f  g"

    
    def table(self):

        self.board = [[ [' '],'-------------',[' '],'-----------',[' '] ],
                                            
                     ['     ', [' '],'--------', [' '],'-------',[' '],'   '],
                            
                     ['           ',[' '],'--',[' '],'--',[' '],'           '],

                     [[' '],'',[' '],' ',[' '], '         ',[' '],'',[' '],'',[' ']      ],

                     ['           ',[' '],'--',[' '],'--',[' '],'              '],                       

                     ['     ',[' '],'--------', [' '],'-------',[' '],'    '],

                    [ '  ',[' '],'-------------',[' '],'------------',[' '] ]     ] 
    
    def view(self):
        cont = 0
        for element in self.board:
            self.view_board += '\n'
            for row in element:
                self.view_board += str(row)
        return self.view_board

    def  move_piece(self):
        self.piece_color = piece.Pieces_color()
        for row in self.board:
            for box in row:
                if isinstance(box,list) and box == [' ']:
                    box.pop()
                    box += self.piece_color
                elif isinstance(box,str):
                    box = box
                else:
                    print('nose puede mover aqui ya hay una piesa')
        return self.board


table_p = Board()
table_p.table()
table_p.move_piece()

print(table_p.view())
