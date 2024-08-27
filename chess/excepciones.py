
#jeraquia de invalidmove de rook,piece,pawn pero todas son movimientos invalidos pero algunas especificos
class InvalidMove(Exception):  # Funciones para manejar excepciones estándar
    pass

class InvalidMoveNoPiece(InvalidMove):  #Excepción para un movimiento desde una casilla vacía.
    ...

class InvalidMoveRookMove(InvalidMove): #Excepción para un movimiento inválido de la torre.
    ...




#guardado en raise es opcional no es un requisito obligatorio