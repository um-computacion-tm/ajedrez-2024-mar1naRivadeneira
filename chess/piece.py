class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board
        
    def __str__(self):         
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
    def get_color(self):
        return self.__color__
    
    #movimientos diagonales 
    
    def valid_positions(self, from_row, from_col, to_col, to_row):
      
      possible_positions = (
         self.possible_positions_dai(from_row, from_col)+ #Diagonal ascendente izquierda
         self.possible_positions_dad(from_row, from_col)+ #Diagonal ascendente derecha
         self.possible_positions_ddi(from_row, from_col)+ #Diagonal descendente izquierda
         self.possible_positions_ddd(from_row, from_col)  #Diagonal desscendente derecha
      )
      return (to_row, to_col) in possible_positions
   
    def possible_positions_dai(self, row, col):
      #movimiento diagonal hacia arriba para la izquierda(fila disminnuye y columna disminuye)
      possibles = []
      next_row = row -1
      next_col = col -1
      while next_row >= 0 and next_col  >= 0:
         other_piece = self.__board__.get_piece(next_row, next_col)
         if other_piece is not None:
            #si la pieza es del oponente, puede capturarla
            if other_piece.__color__ != self.__color__:
               possibles.append((next_row, next_col))
            #si hay una pieza amiga o enemiga, no puede seguir mas alla 
            break
         # si la celda esta vacia, la agrega como una posicion posible
         possibles.append((next_row, next_col)) 
         next_row -= 1
         next_col -= 1
      return possibles
   
    
    
   