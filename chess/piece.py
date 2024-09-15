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
      
      possible_diagonal_positions = (
         self.possible_positions_dai(from_row, from_col)+ #Diagonal ascendente izquierda
         self.possible_positions_dad(from_row, from_col)+ #Diagonal ascendente derecha
         self.possible_positions_ddi(from_row, from_col)+ #Diagonal descendente izquierda
         self.possible_positions_ddd(from_row, from_col)  #Diagonal desscendente derecha
      )
      return (to_row, to_col) in possible_diagonal_positions
   
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
   
    def possible_positions_dad(self, row, col):
      #movimiento diagonal hacia arriba para la derecha(fila disminuye y columna aumenta)
      possibles = []
      next_row = row -1
      next_col = col +1
      while next_row >= 0 and next_col  >= 0:
         other_piece = self.__board__.get_piece(next_row, next_col)
         if other_piece is not None:
            #si la pieza es del oponente, puede capturarla
            if other_piece.__color__ != self.__color__:
               possibles.append((next_row, next_col))
            #si hay una pieza amiga o enemiga, no puede seguir mas alla 
            break
         possibles.append((next_row, next_col))
         next_row -= 1
         next_col += 1
      return possibles
    
    def possible_positions_ddi(self, row, col):
        # movimiento diagonal hacia abajo a la izquierda (fila aumenta, columna disminuye)
        possibles = []
        next_row = row + 1
        next_col = col - 1
        while next_row < 8 and next_col >= 0:
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))
                # si hay una pieza, no puede seguir más allá
                break
            # Si la celda está vacía, la agrega como una posición posible
            possibles.append((next_row, next_col))
            next_row += 1
            next_col -= 1
        return possibles
    
    
    #Movimientos verticales y horizontales
    
    def valid_positions(self, from_row, from_col, to_row, to_col,):
        
        possible_orthogonal_positions = (
            #movimientos horizontales y verticales
            self.possible_positions_vd(from_row, from_col) +
            self.possible_positions_va(from_row, from_col) +
            self.possible_positions_hd(from_row, from_col) +
            self.possible_positions_ha(from_row, from_col)
         )
        return (to_row, to_col) in possible_orthogonal_positions
     
    def possible_positions_vd(self, row, col):
       #vertical descendente(moverse  hacia abajo en la misma columna)
        possibles = []
        for next_row in range(row + 1, 8):
            # que la celda que sigue no este ocupada..
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

    def possible_positions_va(self, row, col):
       #vertical ascendente(se mueve hacia arriba en la misma columna)
        possibles = []
        for next_row in range(row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break  
            possibles.append((next_row, col))
        return possibles
    
    def possible_positions_hd(self, row, col):
       #horizontal hacia la derecha (moverse hacia la derecha en la misma fila)
        possibles = []
        for next_col in range(col +1, 8):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))
                break
            possibles.append((row, next_col))
        return possibles    
            
    def possible_positions_ha(self, row, col):
       #horizontal izquierda (moverse hacia la izquierda en la misma fila) 
        possibles = []
        for next_col in range(col - 1, -1, -1):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))
                break  
            possibles.append((row, next_col))
        return possibles
    
   