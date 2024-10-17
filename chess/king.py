 
from chess.piece import Piece

class King(Piece):
   white_str = "♔" 
   black_str = "♚"
   
   def get_valid_moves(self, from_row, from_col, to_row, to_col):
      """Comprueba si el movimiento hacia las coordenadas dadas es permitido para el Rey.
        El Rey puede desplazarse una casilla en cualquier dirección (arriba, abajo, izquierda, derecha o diagonal),
        pero no puede moverse a una posición que lo ponga en jaque.
        Parámetros:
        from_row : int
            Fila de la posición actual del Rey en el tablero.
        from_col : int
            Columna de la posición actual del Rey en el tablero.
        to_row : int
            Fila de destino del movimiento.
        to_col : int
            Columna de destino del movimiento.

        Retorna:
        bool:
            True si el movimiento es legal según las reglas del ajedrez para el Rey, False en caso contrario.
               """
      return (to_row, to_col) in self.calculate_king_moves(from_row, from_col)
   
   def calculate_king_moves(self, from_row, from_col):
      """Calcula los movimientos válidos para el rey, limitados a un paso en cualquier dirección.
            Args:
               from_row (int): Fila de origen.
               from_col (int): Columna de origen.
            
            Returns:
               list of tuple: Lista de movimientos válidos."""
      return self.calculate_moves(from_row, from_col, self.__all_directions__, single_step=True)