from pieces import Piece
piece = Piece(input('enter one color: ') )
class Board:
    def __init__(self):
        self.board = []
        self.view_board = ''
        self.coordinate = "     0    1     2      3      4    5    6"

    
    def table(self):

        self.board = [[ [' '],'-------------',[' '],'-----------',[' '] ],
                                            
                     ['     ', [' '],'--------', [' '],'-------',[' '],'   '],
                            
                     ['           ',[' '],'--',[' '],'--',[' '],'           '],

                     [[' '],'',[' '],' ',[' '], '         ',[' '],'',[' '],'',[' ']      ],

                     ['           ',[' '],'--',[' '],'--',[' '],'              '],                       

                     ['     ',[' '],'--------', [' '],'-------',[' '],'    '],

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



table_p = Board()
table_p.table()
table_p.move_piece()

print(table_p.view())