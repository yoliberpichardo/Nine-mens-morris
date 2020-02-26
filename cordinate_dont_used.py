class Board:
    # 'los '.' seran considerada como casillas vacias'
    def __init__(self):
        self.board_comp = ''
        self.table = []
        self.coordinate = "   a  b  c  d  e  f  g"
    # esta funcion es la que mustra el tablero
    def view(self):
        cont = 0
        for element in self.table:
            self.board_comp += str(cont)
            for box in element:
                self.board_comp +='  ' + box
            cont +=1
            self.board_comp += '\n'
        self.board_comp += self.coordinate 
    
        return self.board_comp

    # anulando las coordenadas que no seran utilizadas
    def cancel_positions(self):
        for rec in range(7):
            for rec2 in range(7):
                if rec == rec2:
                    self.table[rec][rec2] = '.'
                else:
                    self.table = ' '
        return self.table
            

    # esta funcion crea el tablero
    def board(self):
        for boxes in range(7):
            self.table.append(['.','.','.','.','.','.','.'])
            
        
    
    
    
game = Board()
game.board()
# game.cancel_positions()
print(game.view())

 
