class Board:
    def __init__(self):
        self.board = []
        # self.matriz_board = []
        self.view_board = ''
        self.coordinate = "   a  b  c  d  e  f  g"

    
    def table(self):
        self.board = [[['.'],['------------------'],['.'],['-----------------'],['.']], 
                               [ ['.'],['----------'], ['.'],['----------'],['.']],
                            
                                   [ ['.'],['--'],['.'],['--'],['.']],

                   [ ['.'],[''],['.'],['.'], ['           '],['.'],[''],['.'],[''],['.']],

                                   [ ['.'],['--'],['.'],['--'],['.']],                       

                           [ ['.'],['----------'], ['.'],['----------'],['.']],

                   [ ['.'],['-----------------'],['.'],['-----------------'],['.']]] 
        

    def view(self):

        # cont = 0
        # for element in self.board:
        #     # if cont != 0:
        #     #     self.view_board +='\n'
        #     self.view_board += str(cont)
        #     if isinstance(element,list):
        #         self.view_board += str(element[0:])
        #     else:
        #         self.view_board += ' '+element
        #     cont +=1
        # self.view_board += self.coordinate 
        # return self.view_board

    # def view(self):
    #     self.cache = []
    #     for row in self.board:
    #         for item in row:
    #             self.cache.append(item)
    #     print(' '.join(self.cache))
        for element in self.board:
            self.view_board += str(element)
        return self.view_board

table_p = Board()
table_p.table()
print(table_p.view())
