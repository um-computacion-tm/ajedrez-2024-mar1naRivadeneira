 
from chess.piece import Piece

class King(Piece):
   white_str = "♔" 
   black_str = "♚"
   
   def get_valid_moves(self, from_row, from_col, to_row, to_col):
      """
        Comprueba si el movimiento hacia las coordenadas dadas es permitido para el Rey.
        Este método recibe las coordenadas actuales de el Rey y la casilla de destino. 
        El Rey puede moverse una casilla en cualquier dirección

        Retorna:
        bool:
            Devuelve True si el movimiento es válido según las reglas para el Rey, 
            False en caso contrario.
               """
      positions = self.__all_directions__         
      possible_king_positions = self.calculate_moves(from_row, from_col, positions, single_step = True)
      return (to_row, to_col) in possible_king_positions
   
   