class Piece:
    def __init__(self,symbol):
        self.symbol = symbol
        self.quant = 9

    def quant_piece(self):
        quantity = self.symbol * self.quant
        return quantity


    
