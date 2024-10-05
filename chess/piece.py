class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board
        self.has_moved = False #para verificar los movimientos
        self.__all_directions__= [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
        self.__rook_directions__=  [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.__bishop_directions__= [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
    def __str__(self):         
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
    def get_color(self):
        return self.__color__
    
    def can_eat(self, from_row, from_col):
        # Verifica si hay una pieza del oponente en la posición (from_row, from_col)
        piece = self.__board__.get_piece(from_row, from_col)
        return piece is not None and piece.get_color() != self.get_color()
    
    def general_moves(self, row, col, directions, single_step=False):
        """
        calcula los movimientos generales de la pieza en función de las direcciones especificadas

        row: Fila actual de la pieza.
        col: Columna actual de la pieza.
        directions: Lista de tuplas que representan las direcciones de movimiento.
        single_step: Si es True, la pieza solo puede moverse una casilla en cada dirección.
        return: Lista de tuplas con los movimientos válidos que se pueden hacer
        """
        valid_moves = []

        for dir_row, dir_col in directions:
            next_row, next_col = row + dir_row, col + dir_col
            
            # Mueve en la dirección especificada
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                # Verificar captura de pieza enemiga
                if self.can_eat(next_row, next_col):
                    valid_moves.append((next_row, next_col))  # Puede capturar
                    break  # Detener si se captura una pieza
                
                piece_in_target = self.__board__.get_piece(next_row, next_col)
                if piece_in_target is not None:
                    break
                # Si está vacío, añadir el movimiento
                valid_moves.append((next_row, next_col))
                
                # Si solo se permite un solo paso, salir del bucle
                if single_step:
                    break
                
                # Continuar en la misma dirección
                next_row += dir_row
                next_col += dir_col
                
        return valid_moves
    
    def calculate_moves(self, from_row, from_col, directions, single_step):
        return self.general_moves(from_row, from_col, directions, single_step=single_step)
    
    def get_directions(self):
        #define las direcciones válidas de movimiento para la pieza.
        raise NotImplementedError("Este método debe ser implementado por las pezas")

    
    def is_in_bounds(self, row, col):               
          return 0 <= row < 8 and 0 <= col < 8
      
      #movimientos diagonales generales
      #otro metodo para movimientos ortogonales 
      
    '''#metodo para combinar las posiciones y evitar la duplicacion
    
    def combine_possible_positions(self, position_methods, from_row, from_col):
        possible_positions = []
        for method in position_methods:
            possible_positions += method( from_row, from_col)
        return possible_positions    
    
    #movimientos diagonales 
   
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
      while next_row >= 0 and next_col < 8:
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
    
    def possible_positions_ddd(self, row, col):
    # movimiento diagonal hacia abajo a la derecha (fila aumenta, columna aumenta)
        possibles = []
        next_row = row + 1
        next_col = col + 1
        while next_row < 8 and next_col < 8:
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                # Si hay una pieza del oponente, puede capturarla
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))
                break
            # Si la celda está vacía, la agrega como posible posición
            possibles.append((next_row, next_col))
            next_row += 1
            next_col += 1
        return possibles
    
    
    #Movimientos verticales y horizontales
     
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
'''
   