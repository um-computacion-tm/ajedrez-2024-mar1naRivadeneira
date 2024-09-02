#se mueve solo hacia adelante y captura en diagonal, una casilla a la vez, al inicio puede moverse dos lugares
from chess.piece import Piece

class Pawn(Piece):
     white_str = "♟" 
     black_str = "♙"
   
     def mover(self):
          pass                      
     
     '''def __init__(self, color):
          super().__init__(color)
          self.has_moved = False   #para ver si el peon ha hecho su primer mov
          
     def is_valid_move(self, from_row, from_col, to_col, to_row, board):
          direction = 1 if self.__color__ == 'WHITE' else -1 # el peon blanco se mueve hacia arriba y los negros para abajo     
          
          if from_col == to_col:
               if (to_row - from_row) == direction:
                    return board.get_piece(to_row, to_col) is None #movimiento vertical de una casilla
               if (to_row - from_row) == 2 * direction and not self.has_move:  #movimiento vertical de dos casillas
                    return (board.get_piece(to_row, to_col) is None and 
                            board.get_piece(from_row + direction, to_col) is None)'''