#se mueve en forma de L y puede saltearse otras piezas
from chess.piece import Piece

class Knight(Piece):
   def mover(self):
      pass

   def __str__(self):  #devuelve el simbolo de la torre segun el color de la pieza
      if self.__color__ == "WHITE":
          return "♘"
      else:
         return "♞" 