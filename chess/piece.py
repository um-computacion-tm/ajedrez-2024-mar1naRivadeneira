class Piece:
    def __init__(self, color, board):
        """Inicializa una pieza de ajedrez.
        Args:
            color (str): Color de la pieza ("WHITE" o "BLACK").
            board (Board): Instancia del tablero donde está ubicada la pieza."""
        self.__color__ = color
        self.__board__ = board
        self.has_moved = False # Indica si la pieza ya se ha movido
        self.__all_directions__= [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
        self.__bishop_directions__= [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
    def __str__(self):        
        """Devuelve una representación en cadena de la pieza.
        Returns:
            str: Representación de la pieza basada en su color.""" 
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
    def get_color(self):
        """Obtiene el color de la pieza.
        Returns:
            str: Color de la pieza ("WHITE" o "BLACK")."""
        return self.__color__
    
    def can_eat(self, from_row, from_col):
        """Verifica si la pieza puede capturar otra pieza en la posición dada.
        Args:
            row (int): Fila de la posición a verificar.
            col (int): Columna de la posición a verificar.
        Returns:
            bool: True si puede capturar, False de lo contrario."""
        piece = self.__board__.get_piece(from_row, from_col)
        return piece is not None and piece.get_color() != self.get_color()
    
    def general_moves(self, row, col, directions, single_step=False):
        """
        calcula los movimientos generales de la pieza en función de las direcciones especificadas
          Args:
            row (int): Fila actual de la pieza.
            col (int): Columna actual de la pieza.
            directions (list of tuple): Lista de tuplas que representan las direcciones de movimiento.
            single_step (bool): Si es True, la pieza solo puede moverse una casilla en cada dirección.
        
        Returns:
            list of tuple: Lista de tuplas con los movimientos válidos que se pueden realizar.
        """
        valid_moves = []

        for dir_row, dir_col in directions:
            next_row, next_col = row + dir_row, col + dir_col
            
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                if self.can_eat(next_row, next_col):
                    valid_moves.append((next_row, next_col))  
                    break 
                
                piece_in_target = self.__board__.get_piece(next_row, next_col)
                if piece_in_target is not None:
                    break
            
                valid_moves.append((next_row, next_col))
                
                if single_step:
                    break
                
                next_row += dir_row
                next_col += dir_col
                
        return valid_moves
    
    def calculate_moves(self, from_row, from_col, directions, single_step):
        """Calcula los movimientos válidos utilizando el método general_moves.
        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            directions (list of tuple): Direcciones de movimiento permitidas.
            single_step (bool): Indica si el movimiento es de un solo paso.
        
        Returns:
            list of tuple: Movimientos válidos calculados."""
        return self.general_moves(from_row, from_col, directions, single_step=single_step)
    
    def get_directions(self):
        """Define las direcciones válidas de movimiento para la pieza.
        Raises:
            NotImplementedError: Si el método no es implementado por la subclase."""
        raise NotImplementedError("Este método debe ser implementado por las pezas")

    def is_in_bounds(self, row, col):      
        """  Verifica si una posición está dentro de los límites del tablero.
        Args:
            row (int): Fila de la posición.
            col (int): Columna de la posición.
        
        Returns:
            bool: True si está dentro de los límites, False de lo contrario."""         
        return 0 <= row < 8 and 0 <= col < 8
      
      