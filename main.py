import os
from Board import *
from players import optionPlayer
character = optionPlayer()
table_p = Board()
table_p.table()



def action_instance():
    os.system('cls')
    table_p.view()
    table_p.insert_token(character) # El metodo insert token de tablero toma como parametro character que proviene de la clase player
    os.system('cls')
    
    action_instance() 
action_instance()