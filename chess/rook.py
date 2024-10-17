
from chess.piece import Piece   

class Rook(Piece):
  white_str = "♖"  
  black_str = "♜"    
   
  def get_valid_moves(self, from_row, from_col, to_row, to_col):
    """Verifica si el movimiento de la torre es válido.
    Args:
        from_row (int): Fila de origen.
        from_col (int): Columna de origen.
        to_row (int): Fila de destino.
        to_col (int): Columna de destino.
    Returns:
        bool: True si el movimiento es válido, False en caso contrario"""
    directions = self.is_valid_rook_move()
    possible_moves = self.general_moves(from_row, from_col, directions, single_step=False )
    return (to_row, to_col) in possible_moves

    
  def is_valid_rook_move(self): 
    """  Devuelve las direcciones ortogonales válidas para la torre (vertical y horizontal).
    Returns:
        list of tuple: Lista de direcciones permitidas para el movimiento de la torre"""
    return [(-1, 0), (1, 0), (0, -1), (0, 1)]