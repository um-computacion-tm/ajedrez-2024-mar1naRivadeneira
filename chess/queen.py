
from chess.piece import Piece

class Queen(Piece):
   white_str = "♕" 
   black_str = "♛"
    
   def get_valid_moves(self, from_row, from_col, to_row, to_col):
    """Verifica si un movimiento es válido para la reina.
        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.
        
        Returns:
            bool: True si el movimiento es válido, False de lo contrario."""
    possible_move= self.calculate_moves(from_row, from_col, self.__all_directions__, single_step=False)
    return (to_row, to_col)in possible_move