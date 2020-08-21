from players import *
from os import system
class Board:
    def __init__(self,character):
        self.color_token = [['◉'],['◎']]
        self.row_input = ''
        self.row_destiny = ''
        self.column_input = ''
        self.column_destiny = ''
        self.board = []
        self.view_board = '' 
        self.cont_token_table_w = 0
        self.cont_token_table_b = 0
        self.matriz = []
        self.character = character
        self.token_extracted = ''
        self.checks = ['0','1','2','3','4','5','6'] 
        self.coordinate = "     0    1    2    3    4    5    6"
        self.piece = 0
        self.output = ['exit','Exit','EXIT'] 
    #-------------------------------------------------------------METHOD CREATE MATRIX-----------------------------------------------------#
    def table(self):
        """"The matrix is ​​created and adjusted to its corresponding shape."""
        self.board = [[ [' '],'-----','-----',[' '],'-----','-----',[' '] ],

                     ['  |  ', [' '],'-----', [' '],'-----',[' '],'  | '],

                     ['  |    ','|  ',[' '],[' '],[' '],'  |  ','  |   '],
                                                                                                                              
                     [[' '],[' '],[' '], '     ',[' '],[' '],[' ']],

                     ['  |    ','|  ',[' '],[' '],[' '],'  |   ',' |   '],

                     ['  |  ', [' '],'-----', [' '],'-----',[' '],'  | '],

                     [[' '], '-----', '-----', [' '], '-----', '-----', [' ']]]
        return self.board
    #-----------------------------------METHOD THAT ALLOWS PLAYERS TO PERCEIVE THE PERFECT VIEW OF THE BOARD-------------------------------------------------------------#
    def view(self):
        """This improved view method adds excellent order and view to the dashboard.""" 
        system('cls')
        cont = 0
        """The following conditional causes each player's name and number of chips to be displayed when the chip movement process begins."""
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
    #------------------------------------------------METHOD FOR CLEANING OF SCREEN----------------------------------------#
    def clean_screen1(self):
        """We use this method to call it in each case that the screen needs to be cleaned."""
        system('cls')
        self.view_board = ''
        print(self.view())
    #-----------------------------------------------METHOD FOR ENTERING TABS IN THE BOARD-------------------------------------------------------------------#
    def input_coordinate(self):
        """As input this method receives the, where you want to add a file of said player."""
        self.row_input = input('Enter the row: ')
        self.column_input = input('Enter the column: ') 
        if self.row_input in self.output or self.column_input in self.output:
            system('cls')
            exit()
        elif self.row_input not in self.checks or self.column_input not in self.checks:
            self.clean_screen1()
            print('Ohh ray!!, You cannot enter letters or digits of two numbers')
            self.input_coordinate()
        else:
            self.matriz = self.board[int(self.row_input)][int(self.column_input)]
            return self.matriz
    #-----------------------------------------------METHOD FOR INSERTING THE TAB IN THE BOARD AND SUM OF TABS--------------------------------------------------#
    def insert_token(self,character):
        """Insert token calls the function for entering coordinates,
    and verifies if these entries are valid as well as the sum of the number of tokens of each player."""
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
    #-------------------------------------------METHOD FOR CHANGE OF TURN----------------------------------------------------------------------------------#
    def change_turn(self):
        """A request is made to the functions of the mills in this space, then the turn is managed,
    if it happens to be the first player's file then the turn will pass to the second one but it will return to the previous player and so on."""
        self.checMill_rows()
        self.checMill_colums()
        while self.character:
            if self.character == playerList[0].colorTokens:
                self.character = playerList[1].colorTokens
                return self.character
            else:
                self.character = playerList[0].colorTokens
                return self.character
    #-------------------------------------METHOD THAT MANAGES THE TURN AND THE ADDITION OF THE NUMBER OF FILES---------------------------------------------#
    def run_insert_token(self):
        """The character variable contains the player's chip 1,
    shows its name and then the sum of each player's chips is made."""    
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
    #--------------------------------------------------METHOD IN CHARGE OF THE FILE MOVEMENT---------------------------------------------------------------#
    def input_to_select_token(self):
        """ According to each player's turn this function asks for the coordinates to select the tile to move
    and then adds it to the board, we added a loop to verify those inputs so they are always valid inputs."""
        print('Select a piece on board to move')
        self.matriz = []
        self.view_board = ''
        if self.character == playerList[1].colorTokens:
            self.row_select = input('Enter the row to move the token: ')
            self.column_select = input('Enter the column to move the token: ')
            if self.row_select in self.output or self.column_select in self.output:
                system('cls')
                exit()
            elif self.row_select not in self.checks or self.column_select not in self.checks:
                self.clean_screen1()
                print('Ohh ray!, You cannot enter letters or digits of two numbers')
                self.input_to_select_token()
            if self.board[int(self.row_select)][int(self.column_select)] == ['◉']:
                self.token_extracted = self.board[int(self.row_select)][int(self.column_select)]
                return self.token_extracted
                self.run_insert_token()
            else:
                self.cleaning_piece()
            """Turn corresponding to player 1 and we show his name."""
        else:   
            print('TURN OF → {}'.format(playerList[1].name))
            self.row_select = input('Enter the row to move the token: ')
            self.column_select = input('Enter the column to move the token: ')
            if self.row_select in self.output or self.column_select in self.output:
                system('cls')
                exit()
            elif self.row_select not in self.checks or self.column_select not in self.checks:
                self.clean_screen1()
                print('Ohh ray!, You cannot enter letters or digits of two numbers')
                self.input_to_select_token()
            if self.board[int(self.row_select)][int(self.column_select)] == ['◎']:
                self.token_extracted = self.board[int(self.row_select)][int(self.column_select)]
                return self.token_extracted
            else:
                self.cleaning_piece()
    #---------------------------------------METHOD THAT HANDLES TOKEN POSSESSION-------------------------------------------------------------------------------#
    def cleaning_piece(self):
        """Firstly, the conditional verifies if the piece that a player took is his own property,
    if not, then he will give an alert message that it is not his piece."""
        if self.board[int(self.row_select)][int(self.column_select)] == ['◎']: 
            print('This is not your file or not a list, choose your corresponding file..')
            input('Press enter for continue:  ')
            system('cls')
            print(self.view())
            print('TURN OF → {}'.format(playerList[0].name))
            self.input_to_select_token()
        else:
            print('This is not your file or not a list, choose your corresponding file..')
            input('Press enter for continue:  ')
            self.clean_screen1()
            self.input_to_select_token()
    #-----------------------------------------------METHOD THAT HANDLES THE DESTINATION WHERE YOU WANT TO MOVE A TAB-----------------------------------------------#
    def movement_adjacent_tiles(self):
        """These data entries will store the coordinates that will be the positions where you want to take the file."""
        self.row_destiny = input('Enter the row of destiny: ')
        self.column_destiny = input('Enter the column of destiny: ')
        if self.row_destiny in self.output or self.column_destiny in self.output:
            system('cls')
            exit()
        elif self.row_destiny not in self.checks or self.column_destiny not in self.checks:
            self.clean_screen1()
            print('Ohh ray!!, You cannot enter letters or digits of two numbers')
            self.movement_adjacent_tiles()
        y1 = int(self.row_select)
        x1 = int(self.column_select)
        y2 = int(self.row_destiny)
        x2 = int(self.column_destiny)
        if (self.board[y2][x2] == [' ']):
            if (y1 == 0) or (y1 == 6) or (x1 == 0) or (x1 == 6):#colums 0 and 6, rows 0 and 6
                if (x1 + 3 == x2 and y1 == y2) or (y1 + 3 == y2 and x1 == x2):
                    self.add_tab_on_the_board(x2,y2)
                    return
                elif (x1 - 3 == x2 and y1 == y2) or (y1 - 3 == y2 and x1 == x2):
                    self.add_tab_on_the_board(x2,y2)
                    return
            if (y1 == 2 or y1 == 3) or (y1 == 4) or (x1 == 2 or x1 == 3) or (x1 == 4):#colums 2,4 and 3; rows 2,4 and 3
                if (x1 + 1 == x2 and y1 == y2) or (y1 + 1 == y2 and x1 == x2):
                    self.add_tab_on_the_board(x2,y2)
                    return 
                elif (x1 - 1 == x2 and y1 == y2) or (y1 - 1 == y2 and x1 == x2):
                    self.add_tab_on_the_board(x2,y2)
                    return 
            if (y1 == 1) or (y1 == 5) or (x1 == 1) or (x1 == 5):
                if (x1 + 2 == x2 and y1 == y2) or (y1 + 2 == y2 and x1 == x2):#colums 1 and 5, rows 1 and 5
                    self.add_tab_on_the_board(x2,y2)
                elif (x1 - 2 == x2 and y1 == y2) or (y1 - 2 == y2 and x1 == x2):
                    self.add_tab_on_the_board(x2,y2)
                    return 
            else:
                self.clean_screen() 
        else:
            self.clean_screen1()
            print('It not is a list, reenter..')
            self.movement_adjacent_tiles()
    #---------------------------------------------------------METHOD ADD TAB ON THE BOARD------------------------------------------------------------------------#
    def add_tab_on_the_board(self,x2,y2): 
        """The extracted tab variable saves the selected tab that you want to move to a destination,
    and is later added to the board."""
        self.token_extracted = self.board[int(self.row_select)][int(self.column_select)].pop()
        self.board[int(self.row_select)][int(self.column_select)].append(' ')
        self.board[y2][x2].pop()
        self.board[y2][x2].append(self.token_extracted)
        self.token_extracted = ''
        self.matriz = self.board[y2][x2]
        return self.matriz
        # self.movement_adjacent_tiles()
    #--------------------------------------------------METHOD FOR CLEAN SCREEN IN ADJACENT LINES--------------------------------------------------------------------#
    def clean_screen(self):
        """In first order the general screen cleaning function is called,
    and as output the function prints the error message that it cannot move on adjacent lines."""
        self.clean_screen1()
        print("Invalid movement, you can only move in adjacent lines")
        self.movement_adjacent_tiles()
    #---------------------------------------------------------METHOD FOR DELETE PIECE PLAYER-------------------------------------------------------------------------#
    def delete_player_piece(self):
        """The inputs received from the player are the coordinates of the chip to be removed from the opposing player."""
        print('Click on foes piece to remove it.!')
        row1 = input('Enter row delete element: ')
        colum2 = input('Enter colums delete element: ')
        if row1 in self.output or colum2 in self.output:
            system('cls')
            exit()
        elif row1 not in self.checks or colum2 not in self.checks:
            self.clean_screen1()
            print('Inputs are not correct coordinates, re-enter!')
            self.delete_player_piece()
        if self.piece != self.board[int(row1)][int(colum2)]:
            self.a = self.board[int(row1)][int(colum2)]
            self.matriz = self.board[int(row1)][int(colum2)].pop()
            self.matriz = self.board[int(row1)][int(colum2)].append(' ')
            self.clean_screen1()
            return self.matriz
        else:
            print('Select an opponent tile to remove..')
            input('Press enter for continue..!')
            self.clean_screen1()
            self.delete_player_piece()          
    #----------------------------------------------------------METHOD FOR RANGES OF THE MATRIX--------------------------------------------------------------------------#
    def ranget(self, a, b, x, y):
        """Block of code that fulfills the function of not leaving the range of the matrix,
    when adding the positions from the mills function."""
        if y + 4 > a:
            return False
        elif y - 3 < 0:
            return False
        else:
            return True
    #------------------------------------------------------------METHOD HORIZONTAL MILLS METHOD-------------------------------------------------------------------------#
    def checMill_rows(self):
        """-Going through the matrix and verifying with the iterators the possible mills formed,
    if a mill has been found, then a request is made to the chip removal function."""
        if self.character == playerList[0].colorTokens:
            w = ['◉']
        else:
            w = ['◎']
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y] == w and self.ranget(7, 7, x, y):
                    if self.board[x][y] and self.board[x][y+3] == w:
                        if self.board[x][y-3] == w:
                            self.piece = w
                            self.delete_player_piece()
                            
                    if self.board[x][y] and self.board[x][y+2] == w:
                        if self.board[x][y-2] == w:
                            self.piece = w
                            self.delete_player_piece()

                    if self.board[x][y] and self.board[x][y+1] == w:
                        if self.board[x][y-1] == w:
                            self.piece = w
                            self.delete_player_piece()
                    
                if self.board[3][0] == w and self.board[3][0+1] == w:
                    if self.board[3][1+1] == w:
                        self.piece = w
                        self.delete_player_piece()

                if self.board[3][4] == w and self.board[3][4+1] == w:
                    if self.board[3][5 + 1] == w:
                        self.piece = w
                        self.delete_player_piece()
            
    #-------------------------------------------------------VERTICAL MILLS METHOD------------------------------------------------------------------#
    def checMill_colums(self): 
        """-Going through the matrix and verifying with the iterators the possible mills formed,
            if a mill has been found, then a request is made to the chip removal function."""
        if self.character == playerList[0].colorTokens:
            w = ['◉']
        else:
            w = ['◎']
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if y != 3:
                    if x + 3 < len(self.board):
                        if self.board[x][y] == w and self.board[x+3][y] == w:
                            if self.board[x-3][y] == w:
                                self.piece = w
                                self.delete_player_piece()

                        if self.board[x][y] == w and self.board[x+2][y] == w:
                            if self.board[x-2][y] == w:
                                self.piece = w
                                self.delete_player_piece()

                        if self.board[x][y] == w and self.board[x+1][y] == w:
                            if self.board[x-1][y] == w:
                                self.piece = w
                                self.delete_player_piece()

                if self.board[0][3] == w and self.board[1][3] == w:
                    if self.board[2][3] == w:
                        self.piece = w
                        self.delete_player_piece()
                        
                if self.board[4][3] == w and self.board[5][3] == w:
                    if self.board[6][4-1] == w:
                        self.piece = w
                        self.delete_player_piece()
    #--------------------------------------------METHOD FOR GENERAL CALL OF ALL THE ABOVE METHODS---------------------------------------------------------#
    def run_move_token(self):
        """"Call of each of the previous methods in order of execution."""
        self.run_insert_token()
        self.input_to_select_token()
        self.movement_adjacent_tiles() 
        system('cls')
        self.view_board = ''
        print(self.view)
        while (self.cont_token_table_b + self.cont_token_table_w) != 0:
            self.run_insert_token()
            self.input_to_select_token()
            self.movement_adjacent_tiles()
            system('cls')
            self.view_board = ''
            print(self.view)