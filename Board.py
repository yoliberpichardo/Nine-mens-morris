from players import *
from os import system

token = Player(' ')

class Board:
    def __init__(self,character):
        self.row_input = ''
        self.column_input = ''
        self.board = []
        self.view_board = '' 
        self.matriz = []
        self.character = character
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
        system('cls')
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
        self.column_input = str(input('enter column: '))
        
        checks ='0123456'
        while self.row_input not in checks or self.column_input not in checks and self.row_input == '' or self.column_input == '':
            print('no se pueden entrar letras o digitos de dos numeros')
            self.row_input = input('enter row: ')
            self.column_input =input('enter column: ')
            system('cls')
        self.matriz = self.board[int(self.row_input)][int(self.column_input)]  
        return self.matriz
        
                        
    # funcion para que el player puda insertar un token

    def insert_token(self,character):
        input_piece = self.input_coordinate()
        if input_piece:
            system('cls')
            while not isinstance(self.board[int(self.row_input)][int(self.column_input)],list):
                print('no se puede introducir esa pieza aqui, vuelva ha poner las coordenadas')
                self.input_coordinate()
                
            self.matriz.pop()
            self.matriz.append(self.character)
            
            return self.matriz
        
            
    def change_turn(self):
        print(self.view())
        while self.insert_token(self.character):
            print(self.view()) 
            self.view_board = ''
            if self.character == token.colorTokens[0] and self.character != '◎':
                self.character = token.colorTokens[1]
                print(self.view())
                self.view_board = ''
                return self.insert_token(self.character),self.view_board
            else:
                self.character = token.colorTokens[0]
                print(self.view())
                self.view_board = ''
                return self.insert_token(self.character),self.view_board
    

    def run_table(self):
        while token.tokens != 0:
            
            if self.change_turn():
                token.tokens -= 1
                self.change_turn()
            else:
                print('no cambió de turno')


    
   
            

    
    
   
table_p = Board(token.colorTokens[0])
table_p.table()
mapper_tokens()
table_p.run_table()
print(table_p.view())

