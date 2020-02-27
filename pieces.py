class Piece:
    def __init__(self,color):
        self.color = color
        self.character = ['●','O'] 

    def Pieces_color(self):
        if self.color == 'black':
            return self.character[0]
        elif self.color == 'white':
            return self.character[1]

