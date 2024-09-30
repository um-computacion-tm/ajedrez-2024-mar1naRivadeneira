#Se mueve en forma de "L"
from chess.piece import Piece

class Knight(Piece): 
   white_str = "♘"  
   black_str = "♞"
  
   def possible_moves(self, row, col):
        """
        Calcula todos los movimientos posibles para el caballo desde la posición actual (row, col).
        """
        # Todas las posibles direcciones del movimiento en forma de "L"
        directions = [
            (-2, -1), (-2, 1),  # Arriba a la izquierda, arriba a la derecha
            (-1, -2), (-1, 2),  # Izquierda arriba, derecha arriba
            (1, -2), (1, 2),    # Izquierda abajo, derecha abajo
            (2, -1), (2, 1)     # Abajo a la izquierda, abajo a la derecha
        ]
        # Obtener los movimientos válidos
        return [
            (row + dir_row, col + dir_col)
            for dir_row, dir_col in directions
            if self.is_in_bounds(row + dir_row, col + dir_col) and 
               (not self.is_occupied(row + dir_row, col + dir_col) or self.can_eat(row + dir_row, col + dir_col))
        ]
        '''return self.get_knight_moves(row, col, directions)'''
        
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