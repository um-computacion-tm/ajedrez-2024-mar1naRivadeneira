#puede moverse en vertical o horizontal en cualquier casilla pero de la misma columna o fila
from piece import Piece   

class Rook(Piece):
   def mover(self):
      pass

   def is_valid_move(self, from_row, from_col, to_row, to_col, board):
      if from_col == to_col:
         step = 1 if to_row > from_row else -1
         for row in range(from_col + step, to_col, step):
            if board.get_piece(row, from_col ) is not None:
               return False
         return True   