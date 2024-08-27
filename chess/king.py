#se mueve vertical, horizontal y vertical pero solo de a una casilla
from chess.piece import Piece

class King(Piece):
   def mover(self):
      pass

   def __str__(self):  #devuelve el simbolo de la torre segun el color de la pieza
      if self.__color__ == "WHITE":
          return "♔"
      else:
         return "♚" 