from players import *
from os import system

class Board:
    def __init__(self,character):
        self.row_input = ''
        self.row_of_destiny = ''
        self.column_input = ''
        self.column_of_destiny = ''
        self.board = []
        self.view_board = '' 
        self.cont_token_table_w = 0
        self.cont_token_table_b = 0
        self.matriz = []
        self.character = character
        self.token_extracted = ''
        self.checks = ['0','1','2','3','4','5','6']
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

        while self.row_input not in self.checks or self.column_input not in self.checks :
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
            if self.character == '◉':
                self.cont_token_table_w += 1
            else:
                self.cont_token_table_b += 1
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
                    
    def run_insert_token(self):
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
                self.view_board = ''
            else:
                print('TURN OF → {}'.format(playerList[0].name))
                self.view_board = ''
        self.change_turn()
        return self.matriz

    def input_to_select_token(self):
        self.run_insert_token()
        system('cls')
        self.view_board = ''
        print(self.view())
        self.matriz = []
        self.row_select = input('Enter the row to move the token: ')
        self.column_select = input('Enter the column to move the token: ')  

        while self.row_select not in self.checks or self.column_select not in self.checks :
            print('Ohh ray!!, You cannot enter letters or digits of two numbers')
            self.row_select = input('Enter the row to move the token: ')
            self.column_select = input('Enter the column to move the token: ')
            system('cls')
            self.view_board = ''
            print(self.view())
        self.matriz = self.board[int(self.row_select)][int(self.column_select)]
        return self.matriz
        
    def extract_token(self):
        self.input_to_select_token()
        system('cls')
        self.view_board = ''
        print(self.view())
        while not isinstance(self.board[int(self.row_select)][int(self.column_select)],list):
            system('cls')
            self.view_board = ''
            print(self.view())
            print('You cant enter that piece here, re-enter the coordinates')
            self.input_to_select_token()

        if self.board[int(self.row_select)][int(self.column_select)] != [' ']:
            self.token_extracted += self.board[int(self.row_select)][int(self.column_select)].pop()
            self.board[int(self.row_select)][int(self.column_select)].append(' ')
            return self.token_extracted
        else:
            self.view_board = ''
            print(self.view())
            print('box incorrect, re-enter the coordinates')
            self.extract_token()
    
    def input_to_move_token(self):
        self.extract_token()
        system('cls')
        self.view_board = ''
        print(self.view())
        self.matriz = []
        self.row_of_destiny = input('Enter the row of destiny: ')
        self.column_of_destiny = input('Enter the column of destiny: ')
        
        while self.row_of_destiny not in self.checks or self.column_of_destiny not in self.checks :
            print('Ohh ray!!, You cannot enter letters or digits of two numbers')
            self.row_of_destiny = input('Enter the row of destiny: ')
            self.column_of_destiny = input('Enter the column of destiny: ')
            system('cls')
            self.view_board = ''
            print(self.view())
        self.matriz = self.board[int(self.row_of_destiny)][int(self.column_of_destiny)]
        return self.matriz

    def move_token(self):
        self.input_to_move_token()
        system('cls')
        self.view_board = ''
        print(self.view())
        while not isinstance(self.board[int(self.row_of_destiny)][int(self.column_of_destiny)],list):
            self.view_board = ''
            print(self.view())
            print('You cant enter that piece here, re-enter the coordinates')
            self.input_to_move_token()

        if self.board[int(self.row_of_destiny)][int(self.column_of_destiny)] == [' ']:
            self.board[int(self.row_of_destiny)][int(self.column_of_destiny)].pop()
            self.board[int(self.row_of_destiny)][int(self.column_of_destiny)].append(self.token_extracted)
            self.token_extracted = ''
            self.matriz = self.board[int(self.row_of_destiny)][int(self.column_of_destiny)]
            return self.matriz

        else:
            self.view_board = ''
            print(self.view())
            print('box incorrect, re-enter the coordinates')
            self.extract_token()
    
    def run_move_token(self):
        self.move_token()
        system('cls')
        self.view_board = ''
        print(self.view)
        while (self.cont_token_table_b + self.cont_token_table_w) != 0:
            self.move_token()
            system('cls')
            self.view_board = ''
            print(self.view)
        