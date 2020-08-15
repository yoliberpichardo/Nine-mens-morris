from Board import *
from players import *
##We import methods from the board module and the players module
print('Welcome to the famous game NINE MENS MORRIS !!'.upper()+'\n')
##Game welcome
input('Press Enter...')

print(mapper_tokens())

table_p = Board(playerList[0].colorTokens)
table_p.table()
table_p.run_move_token()
print(table_p.view())

#-------------------------------------------------------------------------------MAIN MODULE---------------------------------------------------------------------------------#