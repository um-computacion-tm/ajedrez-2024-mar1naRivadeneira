#Se mueve en forma de "L"
from chess.piece import Piece

class Knight(Piece): 
   white_str = "♘"  
   black_str = "♞"
  
   def get_valid_moves(self, from_row, from_col):
        # se mueve en forma de L= 2 en una dirección y 1 en la otra
        directions = [
            (-2, -1), (-2, 1), (2, -1), (2, 1),
            (-1, -2), (-1, 2), (1, -2), (1, 2)
        ]
        
        valid_moves = []
        
        for dir_row, dir_col in directions:
            next_row, next_col = from_row + dir_row, from_col + dir_col
            if self.is_in_bounds(next_row, next_col):
                target_piece = self.__board__.get_piece(next_row, next_col)
                # El caballo puede moverse si la casilla está vacía o si puede capturar una pieza
                if target_piece is None or target_piece.get_color()!= self.get_color():
                    valid_moves.append((next_row, next_col))
        
        return valid_moves

   '''def get_knight_moves(self, row, col, directions):
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