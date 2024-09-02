from chess.rook import Rook
from chess.pawn import Pawn
from chess.queen import Queen
from chess.king import King
from chess.bishop import Bishop
from chess.knight import Knight

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Rook("BLACK", self) # Black
        self.__positions__[0][7] = Rook("BLACK", self) # Black
        self.__positions__[7][7] = Rook("WHITE", self) # White
        self.__positions__[7][0] = Rook("WHITE", self) # White
        
        self.__positions__[0][1] = Knight("BLACK", self) # Black
        self.__positions__[0][6] = Knight("BLACK", self) # Black
        self.__positions__[7][1] = Knight("WHITE", self) # White
        self.__positions__[7][6] = Knight("WHITE", self) # White
        
        self.__positions__[0][2] = Bishop("BLACK", self) # Black
        self.__positions__[0][5] = Bishop("BLACK", self) # Black
        self.__positions__[7][2] = Bishop("WHITE", self) # White
        self.__positions__[7][5] = Bishop("WHITE", self) # White
        
        self.__positions__[0][3] = Queen("BLACK", self) # Black
        self.__positions__[7][3] = Queen("WHITE", self) # White
        
        self.__positions__[0][4] = King("BLACK", self) # Black
        self.__positions__[7][4] = King("WHITE", self) # White
        
        for col in range(8):
            self.__positions__[1][col]= Pawn("BLACK", self)
            self.__positions__[6][col]= Pawn("WHITE", self)
            
    def __str__(self): 
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str
         
    def get_piece(self, row, col):
          return self.__positions__[row][col]
      
    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece