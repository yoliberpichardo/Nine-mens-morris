class Board:
    def __init__(self):
        self.board = []
        self.piece = ''
        self.view_board = ''
        self.coordinate = "   a  b  c  d  e  f  g"

    
    def table(self):

        self.board = [[ [],'-------------',[],'-----------',[] ],
                                            
                     ['     ', [],'--------', [],'-------',[],'   '],
                            
                     ['           ',[],'--',[],'--',[],'           '],

                     [[],'',[],' ',[], '         ',[],'',[],'',[]      ],

                     ['           ',[],'--',[],'--',[],'              '],                       

                     ['     ',[],'--------', [],'-------',[],'    '],

                    [   '',[],'-------------',[],'------------',[] ]     ] 
    
    def view(self):
        cont = 0
        for element in self.board:
            self.view_board += '\n'
            for row in element:
                self.view_board += str(row)
        return self.view_board

    def pieces(self):
        for row in self.board:
            for box in row:
                if isinstance(box,list) and box == []:
                    box += self.piece
                elif isinstance(box,str):
                    box = box
                else:
                    print('no se puede mover aqui')
        return self.board


table_p = Board()
table_p.table()
table_p.pieces()
print(table_p.view())
