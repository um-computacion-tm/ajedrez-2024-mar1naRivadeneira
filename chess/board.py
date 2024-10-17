from chess.rook import Rook
from chess.pawn import Pawn
from chess.queen import Queen
from chess.king import King
from chess.bishop import Bishop
from chess.knight import Knight
from chess.excepciones import OutOfBoard

class Board:
    def __init__(self, for_test = False): 
        """Inicializa un tablero de ajedrez con las piezas en su posicion inicial.
        
        Args:
            for_test (bool): Si es True, el tablero se inicializa vacio"""
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:    
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
        """Devuelve una representacion en cadena del tablero.
              Returns:
                    str: Representacion del tablero con las piezas y las posiciones vacias"""
        board_str = "  0 1 2 3 4 5 6 7\n"
        for row_index, row in enumerate(self.__positions__):
            board_str += f"{row_index} " 
        
            for col_index, cell in enumerate(row):
                if cell is not None:
                    board_str += f"{cell} "
                else:
                    board_str += ". " 
                    
            board_str += f"{row_index}\n"        
                    
        board_str += "  0 1 2 3 4 5 6 7"  
        return board_str
    
    def get_piece(self, row, col):
        """Devuelve la pieza en la posición indicada.
        Args:
            row (int): Fila de la pieza.
            col (int): Columna de la pieza.
        
        Returns:
            Piece: La pieza en la posición (row, col) o None si está vacía.
        
        Raises:
            OutOfBoard: Si la posición está fuera del tablero."""
        if not (
            0 <= row < 8 and 0 <= col < 8
        ):
            raise OutOfBoard()
        return self.__positions__[row][col]
      
    def set_piece(self, row, col, piece):
        """Coloca una pieza en la posición especificada.
        Args:
            row (int): Fila de destino.
            col (int): Columna de destino.
            piece (Piece): La pieza a colocar."""
        self.__positions__[row][col] = piece
        
    def move(self, from_row, from_col, to_row, to_col):
        """ Mueve una pieza de una posición a otra.
        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino."""
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)    
            
          
    def has_pieces(self, color):
        """Verifica si quedan piezas de un color en el tablero.
        Args:
            color (str): El color de las piezas a buscar ("WHITE" o "BLACK").
        Returns:
            bool: True si quedan piezas del color especificado, False si no."""
        for row in self.__positions__:
            for piece in row:
                if piece is not None and piece.get_color() == color:
                    return True
        return False            