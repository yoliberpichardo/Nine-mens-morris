def input_to_move_token(self):

    while self.row_of_destiny is self.checks or self.column_of_destiny is self.checks:
        try:
            self.row_of_destiny = input('Enter the row of destiny: ')
            self.column_of_destiny = input('Enter the column of destiny: ')
            self.matriz = self.board[int(self.row_of_destiny)][int(self.column_of_destiny)]
            if self.board[int(self.row_of_destiny)][int(self.column_of_destiny)] != [' ']:
                raise IndexError, "Ingrese otraves, no es una lista "
            break
        except:
            print('Ingrese otraves, no es una lista')
            self.row_of_destiny = input('Enter the row of destiny: ')
            self.column_of_destiny = input('Enter the column of destiny: ')
        
    self.matriz = self.board[int(self.row_of_destiny)][int(self.column_of_destiny)]
    return self.matriz