from Board import *
from players import *

print('Welcome to the famous game NINE MENS MORRIS !!'.upper())
print('The gameplay is: 1 → player vs boot, 2 → player vs player'.upper())

input('Press Enter...')



print(mapper_tokens())

table_p = Board(playerList[0].colorTokens)
table_p.table()
table_p.run_table()
print(table_p.view())