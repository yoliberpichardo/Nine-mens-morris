from players import *
from os import system
class Board:
    def __init__(self,character):
        self.color_token = [['◉'],['◎']]
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

                     [[' '], '-----', '-----', [' '], '-----', '-----', [' ']]]

    #Method to show the perfect view of the board.
    def view(self): 
        system('cls')
        cont = 0
        if playerList[1].colorTokens == '◎' and playerList[1].token == 0:
            print(playerList[0].name,'→',playerList[0].token, playerList[0].colorTokens)
            print(playerList[1].name,'→',playerList[1].token, playerList[1].colorTokens)
        else:
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

    #Method that is responsible for measuring the parameters to enter chips on the board
    def input_coordinate(self):
        self.row_input = input('Enter the row: ')
        self.column_input = input('Enter the column: ')

        while self.row_input not in self.checks or self.column_input not in self.checks:
            print('Ohh ray!!, You cannot enter letters or digits of two numbers')
            self.row_input = input('Enter the row: ')
            self.column_input = input('Enter the column: ')
            system('cls')
            self.view_board = ''
            print(self.view())
        self.matriz = self.board[int(self.row_input)][int(self.column_input)]
        return self.matriz

    #Token removal method.
    def token_removal(self):
        system('cls')
        self.view_board = ''
        print(self.view())
        print("You have a mill, please remove an opponent's tile..")
        self.row_input = input('Enter the row: ')
        self.column_input = input('Enter the column: ')

        while self.row_input not in self.checks or self.column_input not in self.checks:
            print('Ohh ray!!, You cannot enter letters or digits of two numbers')
            self.row_input = input('Enter the row: ')
            self.column_input = input('Enter the column: ')
            system('cls')
            self.view_board = ''
            print(self.view())
        self.matriz = self.board[int(self.row_input)][int(self.column_input)]
        if self.board[int(self.row_input)][int(self.column_input)] != ['']:
            self.board[int(self.row_input)][int(self.column_input)].pop
            print(self.matriz
    #Method for the player to insert a toke
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

    #Method for change turn of players
    def change_turn(self):
            while self.character:
                if self.character == playerList[0].colorTokens:
                    self.character = playerList[1].colorTokens
                    return self.character
                else:
                    self.character = playerList[0].colorTokens
                    return self.character

    #Process that takes care of each player's turn.
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

    #This method is responsible for moving the tiles on the board.
    def input_to_select_token(self):
        system('cls')
        self.view_board = ''
        print(self.view())
        print('Select a piece on board to move')
        self.matriz = []
        self.view_board = ''
        if self.character == playerList[1].colorTokens:
            print('TURN OF → {}'.format(playerList[0].name))
            self.row_select = input('Enter the row to move the token: ')
            self.column_select = input('Enter the column to move the token: ')
            while self.row_select not in self.checks or self.column_select not in self.checks:
                system('cls')
                self.view_board = ''
                print(self.view())
                print('Ohh ray!!, You cannot enter letters or digits of two numbers')
                self.row_select = input('Enter the row to move the token: ')
                self.column_select = input('Enter the column to move the token: ')
            self.matriz = self.board[int(self.row_select)][int(self.column_select)] 

            while not isinstance(self.board[int(self.row_input)][int(self.column_input)],list):
                self.view_board = ''
                print(self.view())
                print('You cant enter that piece here, re-enter the coordinates')
                self.row_select = input('Enter the row to move the token: ')
                self.column_select = input('Enter the column to move the token: ')

            if self.board[int(self.row_select)][int(self.column_select)] == ['◉']:
                self.token_extracted += self.board[int(self.row_select)][int(self.column_select)].pop()
                self.board[int(self.row_select)][int(self.column_select)].append(' ')
                return self.token_extracted
                self.run_insert_token()
            else:
                self.cleaning_piece()

        else:
            print('TURN OF → {}'.format(playerList[1].name))
            self.row_select = input('Enter the row to move the token: ')
            self.column_select = input('Enter the column to move the token: ')
            while self.row_select not in self.checks or self.column_select not in self.checks:
                system('cls')
                self.view_board = ''
                print(self.view())
                print('Ohh ray!!, You cannot enter letters or digits of two numbers')
                self.row_select = input('Enter the row to move the token: ')
                self.column_select = input('Enter the column to move the token: ')
            self.matriz = self.board[int(self.row_select)][int(self.column_select)]
            while not isinstance(self.board[int(self.row_input)][int(self.column_input)],list):
                self.view_board = ''
                print(self.view())
                print('You cant enter that piece here, re-enter the coordinates')
                self.row_select = input('Enter the row to move the token: ')
                self.column_select = input('Enter the column to move the token: ')

            if self.board[int(self.row_select)][int(self.column_select)] == ['◎']:
                self.token_extracted += self.board[int(self.row_select)][int(self.column_select)].pop()
                self.board[int(self.row_select)][int(self.column_select)].append(' ')
                return self.token_extracted
            else:
                self.cleaning_piece()

            self.matriz = self.board[int(self.row_select)][int(self.column_select)]
            return self.matriz

    #Wrong parts cleaning method
    def cleaning_piece(self):
        print('This is not your file, choose your corresponding file..')
        input('Enter to continue..')
        self.input_to_select_token()

    #Method that verifies and takes the selected file to the required destination.
    def input_to_move_token(self):
        self.row_of_destiny = input('Enter the row of destiny: ')
        self.column_of_destiny = input('Enter the column of destiny: ')
        if self.row_of_destiny not in self.checks or self.column_of_destiny not in self.checks:
            system('cls')
            self.view_board = ''
            print(self.view())
            print('Ohh ray!!, You cannot enter letters or digits of two numbers')
            self.input_to_move_token()
            self.input_to_select_token()
        self.matriz = self.board[int(self.row_of_destiny)][int(self.column_of_destiny)]

        if self.board[int(self.row_of_destiny)][int(self.column_of_destiny)] != [' ']:
            system('cls')
            self.view_board = ''
            print(self.view())
            print('It cannot be inserted here, it is not a list')
            self.input_to_move_token()
        else:
            #validation for movement adyacent
            if int(self.row_select) == 0 and int(self.column_select) == 0: #casilla 0,0
                if int(self.row_of_destiny) == 0 or int(self.row_of_destiny) == 3:
                    if int(self.column_of_destiny) == 3 or int(self.column_of_destiny) == 0:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 0 and int(self.column_select) == 3: #Box 0,3
                if int(self.row_of_destiny) == 0 or int(self.row_of_destiny) == 1:
                    if int(self.column_of_destiny) == 0 or int(self.column_of_destiny) == 6:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 0 and int(self.column_select) == 6: #Box 0,6
                if int(self.row_of_destiny) == 0 or int(self.row_of_destiny) == 3:
                    if int(self.column_of_destiny) == 3 or int(self.column_of_destiny) == 6:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 1 and int(self.column_select) == 1: #Box 1,1
                if int(self.row_of_destiny) == 1 or int(self.row_of_destiny) == 3:
                    if int(self.column_of_destiny) == 1 or int(self.column_of_destiny) == 3:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 1 and int(self.column_select) == 3: #Box 1,3
                if int(self.row_of_destiny) == 0 or int(self.row_of_destiny) == 1 or int(self.row_of_destiny) == 2:
                    if int(self.column_of_destiny) == 1 or int(self.column_of_destiny) == 5 or int(self.column_of_destiny) == 3:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 1 and int(self.column_select) == 5: #Box 1,5
                if int(self.row_of_destiny) == 1 or int(self.row_of_destiny) == 3:
                    if int(self.column_of_destiny) == 3 or int(self.column_of_destiny) == 5:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 2 and int(self.column_select) == 2: #Box 2,2
                if int(self.row_of_destiny) == 2 or int(self.row_of_destiny) == 3 :
                    if int(self.column_of_destiny) == 2 or int(self.column_of_destiny) == 3:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 2 and int(self.column_select) == 3: #Box 2,3
                if int(self.row_of_destiny) == 1 or int(self.row_of_destiny) == 2 :
                    if int(self.column_of_destiny) == 2 or int(self.column_of_destiny) == 3 or int(self.column_of_destiny) == 4:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 2 and int(self.column_select) == 4: #Box 2,4
                if int(self.row_of_destiny) == 2 or int(self.row_of_destiny) == 3 :
                    if int(self.column_of_destiny) == 3 or int(self.column_of_destiny) == 4:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 3 and int(self.column_select) == 0: #Box 3,0
                if int(self.row_of_destiny) == 0 or int(self.row_of_destiny) == 3 or int(self.row_of_destiny) == 6:
                    if int(self.column_of_destiny) == 0 or int(self.column_of_destiny) == 1:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 3 and int(self.column_select) == 1: #Box 3,1
                if int(self.row_of_destiny) == 1 or int(self.row_of_destiny) == 3 or int(self.row_of_destiny) == 5:
                    if int(self.column_of_destiny) == 0 or int(self.column_of_destiny) == 1 or int(self.column_of_destiny) == 2:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 3 and int(self.column_select) == 2: #Box 3,2
                if int(self.row_of_destiny) == 2 or int(self.row_of_destiny) == 3 or int(self.row_of_destiny) == 4:
                    if int(self.column_of_destiny) == 2 or int(self.column_of_destiny) == 1:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 3 and int(self.column_select) == 4: #Box 3,4
                if int(self.row_of_destiny) == 2 or int(self.row_of_destiny) == 3 or int(self.row_of_destiny) == 4:
                    if int(self.column_of_destiny) == 5 or int(self.column_of_destiny) == 4:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 3 and int(self.column_select) == 5: #Box 3,5
                if int(self.row_of_destiny) == 1 or int(self.row_of_destiny) == 3 or int(self.row_of_destiny) == 5:
                    if int(self.column_of_destiny) == 4 or int(self.column_of_destiny) == 5 or int(self.column_of_destiny) == 6:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 3 and int(self.column_select) == 6: #Box 3,6
                if int(self.row_of_destiny) == 0 or int(self.row_of_destiny) == 3 or int(self.row_of_destiny) == 6:
                    if int(self.column_of_destiny) == 5 or int(self.column_of_destiny) == 6:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 4 and int(self.column_select) == 2: #Box 4,2
                if int(self.row_of_destiny) == 3 or int(self.row_of_destiny) == 4 :
                    if int(self.column_of_destiny) == 2 or int(self.column_of_destiny) == 3:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 4 and int(self.column_select) == 3: #Box 4,3
                if int(self.row_of_destiny) == 5 or int(self.row_of_destiny) == 4:
                    if int(self.column_of_destiny) == 2 or int(self.column_of_destiny) == 3 or int(self.column_of_destiny) == 4:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 4 and int(self.column_select) == 4: #Box 4,4
                if int(self.row_of_destiny) == 3 or int(self.row_of_destiny) == 4:
                    if int(self.column_of_destiny) == 3 or int(self.column_of_destiny) == 4:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 5 and int(self.column_select) == 1: #Box 5,1
                if int(self.row_of_destiny) == 3 or int(self.row_of_destiny) == 5:
                    if int(self.column_of_destiny) == 3 or int(self.column_of_destiny) == 1:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 5 and int(self.column_select) == 3: #Box 5,3
                if int(self.row_of_destiny) == 6 or int(self.row_of_destiny) == 5 or int(self.column_of_destiny) == 4:
                    if int(self.column_of_destiny) == 3 or int(self.column_of_destiny) == 1 or int(self.column_of_destiny) == 5:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 5 and int(self.column_select) == 5: #Box 5,5
                if int(self.row_of_destiny) == 3 or int(self.row_of_destiny) == 5:
                    if int(self.column_of_destiny) == 3 or int(self.column_of_destiny) == 5:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 6 and int(self.column_select) == 0: #Box 6,0
                if int(self.row_of_destiny) == 3 or int(self.row_of_destiny) == 6:
                    if int(self.column_of_destiny) == 0 or int(self.column_of_destiny) == 3:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 6 and int(self.column_select) == 3: #Box 6,3
                if int(self.row_of_destiny) == 6 or int(self.row_of_destiny) == 5:
                    if int(self.column_of_destiny) == 0 or int(self.column_of_destiny) == 3 or int(self.column_of_destiny) == 6:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

            elif int(self.row_select) == 6 and int(self.column_select) == 6: #Box 6,6
                if  int(self.row_of_destiny) == 3 or int(self.row_of_destiny) == 6:
                    if int(self.column_of_destiny) == 3 or int(self.column_of_destiny) == 6:
                        return self.add_tab_on_the_board()
                return self.clean_screen()

    def add_tab_on_the_board(self):  #Function add tab on the board
        self.board[int(self.row_of_destiny)][int(self.column_of_destiny)].pop()
        self.board[int(self.row_of_destiny)][int(self.column_of_destiny)].append(self.token_extracted)
        self.token_extracted = ''
        self.matriz = self.board[int(self.row_of_destiny)][int(self.column_of_destiny)]
        return self.matriz
        self.input_to_move_token()

    #Method for clean screen
    def clean_screen(self):
        system('cls')
        self.view_board = ''
        print(self.view())
        print("Invalid movement, you can only move in adjacent lines")
        self.input_to_move_token()


    def run_move_token(self):
        self.run_insert_token()
        self.input_to_select_token()
        self.input_to_move_token()
        system('cls')
        self.view_board = ''
        print(self.view)
        while (self.cont_token_table_b + self.cont_token_table_w) != 0:
            self.run_insert_token()
            self.input_to_select_token()
            self.input_to_move_token()
            system('cls')
            self.view_board = ''
            print(self.view)