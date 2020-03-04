from pieces import Piece
from os import system

class Board:
    def __init__(self):
        self.board = []
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
    
    def input_coordinate(self):
        row_input = str(input('enter row: '))
        column_input =str(input('enter column: '))
        checks ='0123456'
        for check in  checks:
            if row_input not in checks or column_input not in checks and row_input == '' or column_input == '':
                row_input = input('enter row: ')
                column_input =input('enter column: ')
        self.matriz = self.board[int(row_input)][int(column_input)] 

    # funcion para que el player puda insertar un token

    # def insert_token(self):
    # if isinstance(self.matriz,list):
    #     self.matriz.pop()
    #     self.matriz.append(self..symbol*1)
                    

    
   
table_p = Board()
table_p.table()
print(table_p.view())


