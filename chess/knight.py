#Se mueve en forma de "L"
from chess.piece import Piece

class Knight(Piece): 
   white_str = "♘"  
   black_str = "♞"
  
   def generate_moves_k(self, from_row, from_col):
        # genera los posibles movimientos del caballo en forma de L
        possible_moves = []
        for dr in [-2, -1, 1, 2]:  # Saltos de fila
            for dc in [-2, -1, 1, 2]:  # Saltos de columna
                if abs(dr) != abs(dc):  # Movimientos en L, descartamos los que no sean L
                    possible_moves.append((from_row + dr, from_col + dc))
        return possible_moves

   def is_valid_move_k(self, to_row, to_col):
        # Verificar si el movimiento es válido
        if self.is_in_bounds(to_row, to_col):
            piece_in_target = self.__board__.get_piece(to_row, to_col)
            return piece_in_target is None or self.can_eat(to_row, to_col)
        return False
    
   def get_valid_moves(self, from_row, from_col):
       #devuelve una lista de todos los movimientos validos para el caballo desde una posicion que se da 
        valid_moves = []
        possible_moves = self.generate_moves_k(from_row, from_col)
        
        for to_row, to_col in possible_moves:
            if self.is_valid_move_k(to_row, to_col):
               valid_moves.append((to_row, to_col))
    
        
        return valid_moves
    
''' valid_moves = []
     
        for dir_row, dir_col in directions:
            next_row, next_col = from_row + dir_row, from_col + dir_col
            if self.is_in_bounds(next_row, next_col):
                target_piece = self.__board__.get_piece(next_row, next_col)
                 El caballo puede moverse si la casilla está vacía o si puede capturar una pieza
                if target_piece is None or target_piece.get_color()!= self.get_color():
                    valid_moves.append((next_row, next_col))
        
        return valid_moves

   def get_knight_moves(self, row, col, directions):
        """
        Calcula los movimientos válidos del caballo, filtrando los que están fuera de los límites del tablero
        o los que tienen piezas propias.
        """
        valid_moves = []

        for dir_row, dir_col in directions:
            next_row, next_col = row + dir_row, col + dir_col

            # Verificar que las coordenadas están dentro de los límites del tablero
            if self.is_in_bounds(next_row, next_col):
                # Verificar si la posición está vacía o si hay una pieza oponente para capturar
                if not self.is_occupied(next_row, next_col) or self.can_eat(next_row, next_col):
                    valid_moves.append((next_row, next_col))
        
        return valid_moves'''    