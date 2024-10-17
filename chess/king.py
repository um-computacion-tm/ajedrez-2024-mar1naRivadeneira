 
from chess.piece import Piece

class King(Piece):
   white_str = "♔" 
   black_str = "♚"
   
   def get_valid_moves(self, from_row, from_col, to_row, to_col):
      """Comprueba si el movimiento hacia las coordenadas dadas es permitido para el Rey.
        Este método recibe las coordenadas actuales de el Rey y la casilla de destino. 
        El Rey puede moverse una casilla en cualquier dirección

        Parámetros: 
        - La posición actual del Rey (fila y columna).
        - La posición de destino a la que se desea mover el Rey (fila y columna).

        Retorna:
        bool:
            Devuelve True si el movimiento es válido según las reglas para el Rey, 
            False en caso contrario.
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