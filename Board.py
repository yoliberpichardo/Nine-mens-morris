from players import *
from os import system

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
        print(playerList[0].name, playerList[0].colorTokens * playerList[0].token,'→', playerList[0].token)
        print(playerList[1].name, playerList[1].colorTokens * playerList[1].token,'→', playerList[1].token)  
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
        self.row_input = input('Enter the row: ')
        self.column_input = input('Enter the column: ')    
        checks = ['0','1','2','3','4','5','6']
        while self.row_input not in checks or self.column_input not in checks:
            print('Ohh ray!!, You cannot enter letters or digits of two numbers')
            self.row_input = input('Enter the row: ')
            self.column_input = input('Enter the column: ')
            system('cls')
            self.view_board = ''
            print(self.view())
        self.matriz = self.board[int(self.row_input)][int(self.column_input)]  
        return self.matriz

    # funcion para que el player puda insertar un token
    def insert_token(self,character):
        self.input_coordinate()
        system('cls')
        while not isinstance(self.board[int(self.row_input)][int(self.column_input)],list):
            self.view_board = ''
            print(self.view())
            print('You cant enter that piece here, re-enter the coordinates')
            self.input_coordinate()  
        if self.board[int(self.row_input)][int(self.column_input)] == [' ']:
            self.matriz.pop()
            self.matriz.append(self.character)
            return self.matriz
        else:
            self.view_board = ''
            print(self.view())
            print('Occupied box, re-enter the coordinates')
            self.insert_token(character)

    def change_turn(self):
            while self.character:
                if self.character == playerList[0].colorTokens:
                    self.character = playerList[1].colorTokens
                    return self.character
                else:
                    self.character = playerList[0].colorTokens
                    return self.character
                    
    def run_table(self):
        print(self.view())
        if self.character == playerList[0].colorTokens:
            print('TURN OF → {}'.format(playerList[0].name))
        while(playerList[0].token + (playerList[1].token)) != 0:
            self.insert_token(self.character)
            if self.character == playerList[0].colorTokens:
                playerList[0].token -= 1
            else:
                playerList[1].token -= 1
            self.view_board = ''
            print(self.view())
            self.change_turn()
            if self.character == playerList[1].colorTokens:
                print('TURN OF → {}'.format(playerList[1].name)) 
                
            else:
                print('TURN OF → {}'.format(playerList[0].name))
            self.view_board = ''