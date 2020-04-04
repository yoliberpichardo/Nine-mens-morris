from Board import *
from players import *
print('Welcome to the famous game NINE MENS MORRIS !!'.upper()+'\n')
print('The gameplay is: 1 → player vs boot, 2 → player vs player'.upper()+'\n')

input('Press Enter...')

print(mapper_tokens())

table_p = Board(playerList[0].colorTokens)
table_p.table()
table_p.run_move_token()
print(table_p.view())

<<<<<<< HEAD
=======

>>>>>>> aa44376bbbce8d9d63dcd0d2d75d575857b37d11
