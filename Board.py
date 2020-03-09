from os import system
from players import *
result = Player('')

print('Welcome to this famous game called NINE MENS MORRIS')
print('GAME MODE: 1= PLAYER VS BOOT, OR 2= PLAYER VS PLAYER')
input('Press Enter....')

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
        self.row_input = str(input('Enter the row '+ result.nombre ))
        self.column_input = str(input('Enter the column '+ result.nombre ))
        
        checks ='0123456'
        for check in checks:
            if self.row_input not in checks or self.column_input not in checks and self.row_input == '' or self.column_input == '':
                print('You cannot enter letters or digits of two numbers')
                self.row_input = str(input('Enter the row '+ result.nombre ))
                self.column_input = str(input('Enter the column '+ result.nombre ))
                system('cls')
            self.matriz = self.board[int(self.row_input)][int(self.column_input)]
            system('cls')
            return self.matriz
            print(self.view())
 # funcion para que el player puda insertar un token
    def insert_token(self, character):
      
        self.view_board = ''
        input_piece = self.input_coordinate()
        if input_piece:
            while not isinstance(self.board[int(self.row_input)][int(self.column_input)],list):
                print('Ohh ray!!, you cannot enter a tab here, re-enter the coordinates...')
                self.input_coordinate()
            self.matriz.pop()
            self.matriz.append(character)
            return (self.matriz)

