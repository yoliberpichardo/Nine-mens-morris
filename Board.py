from pieces import Piece
from os import system

player1 = Piece('●')
player2 = Piece('O')
class Board:
    def __init__(self,player):
        self.player = player
        self.board = []
        # self.piece_black = piece.quant_piece()
        # self.piece_white = piece.quant_piece()
        self.matriz = []
        self.view_board = ''
        self.coordinate = "     0    1    2    3    4    5    6"

    
    def table(self):

        self.board = [[ [' '],'-----','-----',[' '],'-----','-----',[' '] ],
                                            
                     ['  |  ', [' '],'-----', [' '],'-----',[' '],'  | '],
                            
                     ['  |    ','|  ',[' '],[' '],[' '],'  |  ','  |   '],

                     [[' '] ,[' '],[' '], '     ',[' '],[' '],[' ']],

                     ['  |    ','|  ',[' '],[' '],[' '],'  |   ',' |   '],                       

                     ['  |  ', [' '],'-----', [' '],'-----',[' '],'  | '],

                     [ [' '],'-----','-----',[' '],'-----','-----',[' '] ]     ] 


    
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
    
    def input_coordinate(self,player):
        row_input = str(input('enter row: '))
        column_input =str(input('enter column: '))
        checks ='0123456' #[0,1,2,3,4,5,6]
        for check in  checks:
            if row_input not in checks or column_input not in checks and row_input == '' or column_input == '':
                print('solo se pueden introducir numeros, de 0 al 6')
                row_input = input('enter row: ')
                column_input =input('enter column: ')
        self.matriz = self.board[int(row_input)][int(column_input)] 

        if self.player.quant <= 9 :
            while self.player.quant != 0:
                if isinstance(self.matriz,list):
                    self.matriz.pop()
                    self.matriz.append(self.player.symbol*1)
                    self.player.quant -= 1
                else:
                    print('no se puede colocar aqui vuelva ha introducir las coordenadas')
                    row_input = input('enter row: ')
                    column_input =input('enter column: ')
                    self.matriz = self.board[int(row_input)][int(column_input)] 
            return self.board
   


table_p = Board(player1)
table_p.table()
table_p.input_coordinate(player1)
print(table_p.view())
