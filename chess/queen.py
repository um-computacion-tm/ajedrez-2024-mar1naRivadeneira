#se mueve vertical,horizontal y diagonal en cualquier casilla
from chess.piece import Piece

class Queen(Piece):
   def mover(self):
      pass

   def __str__(self):  #devuelve el simbolo de la torre segun el color de la pieza
      if self.__color__ == "WHITE":
          return "♕"
      else:
         return "♛" 