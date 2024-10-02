#Combina los movimientos de la torre y el alfil (vertical, horizontal y diagonal).
from chess.piece import Piece

class Queen(Piece):
   white_str = "♕" 
   black_str = "♛"
    
   def possible_moves_queen(self, from_row, from_col, to_row, to_col):
         directions = [
               (1, 0), (-1, 0), (0, 1), (0, -1),  # Vertical y horizontal
               (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonal
         ]
         possible_positions = self.general_moves(from_row, from_col, directions, single_step=False)
         return(to_row, to_col) in possible_positions