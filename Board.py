from players import *
from os import system

character = optionPlayer()

class Board:
    def __init__(self):
        self.row_input = ''
        self.column_input = ''
        self.board = []
        self.view_board = ''
        self.matriz = []
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
        self.row_input = str(input('enter row: '))
        self.column_input =str(input('enter column: '))
        checks ='0123456'
        for check in  checks:
            if self.row_input not in checks or self.column_input not in checks and self.row_input == '' or self.column_input == '':
                print('no se pueden entrar letras o digitos de dos numeros')
                self.row_input = input('enter row: ')
                self.column_input =input('enter column: ')
            self.matriz = self.board[int(self.row_input)][int(self.column_input)]     
        return self.matriz
                        
    # funcion para que el player puda insertar un token

    def insert_token(self):
        input_piece = self.input_coordinate()
        if input_piece:
            while not isinstance(self.board[int(self.row_input)][int(self.column_input)],list):
                print('no se puede introducir esa pieza aqui, vuelva ha poner las coordenadas')
                self.input_coordinate()
            self.matriz.pop()
            self.matriz.append(character)
            return (self.matriz)
    
    
    
                
    
    
   
table_p = Board()
table_p.table()
table_p.insert_token()        
print(table_p.view())


