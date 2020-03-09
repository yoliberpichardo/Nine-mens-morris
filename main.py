from os import system
from Board import *
from players import optionPlayer
character = optionPlayer()
table_p = Board()
table_p.table()



def action_instance():
    system('cls')
    table_p.view()
    # system('cls')
    table_p.insert_token(character) # El metodo insert token de tablero toma como parametro character que proviene de la clase player
    
  
    
    action_instance() 
action_instance()