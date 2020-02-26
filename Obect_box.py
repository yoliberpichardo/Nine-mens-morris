class Board:
    def __init__(self):
        self.board = None
        self.box_f = ' '
        self.box_t = '.'
        self.view_board = ''
        self.coordinate = "   a  b  c  d  e  f  g"

    
    def table(self):
        self.board = [[[self.box_t],[self.box_f],[self.box_f],[self.box_t],[self.box_f],[self.box_f],[self.box_t]],
                      [[self.box_f],[self.box_t],[self.box_f],[self.box_t],[self.box_f],[self.box_t],[self.box_f]],
                      [[self.box_f],[self.box_f],[self.box_t],[self.box_t],[self.box_t],[self.box_f],[self.box_f]],
                      [[self.box_t],[self.box_t],[self.box_t],[self.box_f],[self.box_t],[self.box_t],[self.box_t]],
                      [[self.box_f],[self.box_f],[self.box_t],[self.box_t],[self.box_t],[self.box_t],[self.box_f]],
                      [[self.box_f],[self.box_t],[self.box_f],[self.box_t],[self.box_f],[self.box_t],[self.box_f]],
                      [[self.box_f],[self.box_t],[self.box_f],[self.box_t],[self.box_f],[self.box_f],[self.box_t]],
                      [[self.box_t],[self.box_f],[self.box_f],[self.box_t],[self.box_f],[self.box_f],[self.box_t]]]
        

    def view(self):
        cont = 0
        for element in self.board:
            if cont > 0:
                self.view_board += '\n'
            self.view_board += str(cont)
            for box in element:
                if isinstance(element,list):
                    self.view_board += " " + box
                elif isinstance(element,str):
                    self.view_board +=  "-"
            cont += 1
            # self.view_board += '\n'
        self.view_board += self.coordinate 
        return self.view_board

table_p = Board()
table_p.table()
# table_p.table()
print(table_p.view())
[ [],'------------',[],'------------',[] ],
                                            
                     ['     ', [],'-------', [],'--------',[],'   '],
                            
                     ['         ',[],'---',[],'---',[],'           '],

                     ['  ',[],[],[], '              ',[],[],[]      ],

                     ['         ',[],'---',[],'---',[],'              '],                       

                     ['    ',[],'--------', [],'--------',[],'    '],

                    [  [],'------------',[],'-------------',[] ]     ] 
    