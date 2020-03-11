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
    
    
    def view(self, player):
        system('cls')
        cont = 0
        print(player.playerList[0].name, player.color_white * player.token_white,'→', player.token_white)
        print(player.playerList[1].name, player.color_black * player.token_black,'→', player.token_black )  
        for element in self.board:
            self.view_board += '\n'
            self.view_board += str(cont) + '  '
            cont += 1
            for row in element:
                self.view_board += str(row)
        self.view_board += '\n'
        self.view_board += self.coordinate
        return self.view_board

    def input_coordinate(self, player):
        self.row_input = input('Enter the row: ')
        self.column_input = input('Enter the column: ')    
        checks = ['0','1','2','3','4','5','6']
        while self.row_input not in checks or self.column_input not in checks:
            print('Ohh ray!!, You cannot enter letters or digits of two numbers')
            self.row_input = input('Enter the row: ')
            self.column_input = input('Enter the column: ')
            system('cls')
            self.view_board = ''
            print(self.view(player))
        self.matriz = self.board[int(self.row_input)][int(self.column_input)]  
        return self.matriz

    # funcion para que el player puda insertar un token
    def insert_token(self,character, player):
        self.input_coordinate(player)
        system('cls')
        while not isinstance(self.board[int(self.row_input)][int(self.column_input)],list):
            print('You cant enter that piece here, re-enter the coordinates')
            self.input_coordinate(player)  
        self.matriz.pop()
        self.matriz.append(self.character)
        return self.matriz

    def change_turn(self, player):
            while self.character:
                if self.character == player.color_white:
                    self.character = player.color_black 
                    player.token_black -= 1
                    return self.character
                else:
                    self.character = player.color_white
                    return self.character
                    
    def run_table(self ,player):
        print(self.view(player))
        if self.character == player.color_white:
            print('TURN OF → {}'.format(player.playerList[0].name))
        while(player.token_white + player.token_black) != 0:
            self.insert_token(self.character, player)
            if self.character == player.color_white:
                system('cls')
                player.token_white -= 1
            self.view_board = ''
            print(self.view(player))
            self.change_turn(player)
            if self.character == player.color_black:
                print('TURN OF → {}'.format(player.playerList[1].name))
            else:
                print('TURN OF → {}'.format(player.playerList[0].name))
            self.view_board = ''