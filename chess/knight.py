#Se mueve en forma de "L"
from chess.piece import Piece

class Knight(Piece): 
   white_str = "♘"  
   black_str = "♞"
  
   def get_valid_moves(self, from_row, from_col, to_row, to_col):
       possible_moves = self.calculate_moves(from_row, from_col)
       return (to_row, to_col) in possible_moves
   
   def calculate_moves(self, from_row, from_col):
        valid_moves = []
        
        for row_offset in [-2, -1, 1, 2]:
            col_offset = 3 - abs(row_offset)
            for col_delta in [-col_offset, col_offset]:
                new_row = from_row + row_offset
                new_col = from_col + col_delta
                
                if self.is_in_bounds(new_row, new_col):
                    if self.can_eat(new_row, new_col) or self.__board__.get_piece(new_row, new_col) is None:
                        valid_moves.append((new_row, new_col))
        return valid_moves                
                