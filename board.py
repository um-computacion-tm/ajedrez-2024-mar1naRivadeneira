from rook import Rook
from pawn import Pawn
from queen import Queen
from king import King
from bishop import Bishop
from knight import Knight

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Rook("BLACK") # Black
        self.__positions__[0][7] = Rook("BLACK") # Black
        self.__positions__[7][7] = Rook("WHITE") # White
        self.__positions__[7][0] = Rook("WHITE") # White
        
        self.__positions__[0][1] = Knight("BLACK") # Black
        self.__positions__[0][6] = Knight("BLACK") # Black
        self.__positions__[7][1] = Knight("WHITE") # White
        self.__positions__[7][6] = Knight("WHITE") # White
        
        self.__positions__[0][2] = Bishop("BLACK") # Black
        self.__positions__[0][5] = Bishop("BLACK") # Black
        self.__positions__[7][2] = Bishop("WHITE") # White
        self.__positions__[7][5] = Bishop("WHITE") # White
        
        self.__positions__[0][3] = Queen("BLACK") # Black
        self.__positions__[7][3] = Queen("WHITE") # White
        
        self.__positions__[7][7] = King("BLACK") # Black
        self.__positions__[7][0] = King("WHITE") # White
        
        self.__positions__[1][0] = Pawn("BLACK") # Black
        self.__positions__[1][1] = Pawn("BLACK") # Black
        self.__positions__[1][2] = Pawn("BLACK") # Black
        self.__positions__[1][3] = Pawn("BLACK") # Black
        self.__positions__[1][4] = Pawn("BLACK") # Black
        self.__positions__[1][5] = Pawn("BLACK") # Black
        self.__positions__[1][6] = Pawn("BLACK") # Black
        self.__positions__[1][7] = Pawn("BLACK") # Black
        
        self.__positions__[6][0] = Pawn("WHITE") # White
        self.__positions__[6][1] = Pawn("WHITE") # White
        self.__positions__[6][2] = Pawn("WHITE") # White
        self.__positions__[6][3] = Pawn("WHITE") # White
        self.__positions__[6][4] = Pawn("WHITE") # White
        self.__positions__[6][5] = Pawn("WHITE") # White
        self.__positions__[6][6] = Pawn("WHITE") # White
        self.__positions__[6][7] = Pawn("WHITE") # White

    def get_piece(self, row, col):
        return self.__positions__[row][col]