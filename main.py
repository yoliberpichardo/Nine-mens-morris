from Board import *
from players import *

play = Player('')
print('Welcome to the famous game NINE MENS MORRIS !!'.upper())
print('The gameplay is: 1 → player vs boot, 2 → player vs player'.upper())

input('Press Enter...')



print(mapper_tokens(play))

table_p = Board(play.color_white)
table_p.table()
table_p.run_table(play)
print(table_p.view(player))