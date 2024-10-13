
#jeraquia de invalidmove de rook,piece,pawn pero todas son movimientos invalidos pero algunas especificos
class InvalidMove(Exception):  # Funciones para manejar excepciones estándar
    message = "Movimiento de pieza invalido"
    def __str__(self):
        return self.message

class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    message = "La posicion esta vacia"
    
class SamePosition(InvalidMove):
    message= "No podes mover la pieza a la misma direccion de origen"
    def __str__(self):
        return self.message   
            
class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"

            
