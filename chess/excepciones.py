
#jeraquia de invalidmove de rook,piece,pawn pero todas son movimientos invalidos pero algunas especificos
class InvalidMove(Exception):  # Funciones para manejar excepciones estándar
    message = "Movimiento de pieza invalido"
    def __str__(self):
        return self.message

class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    message = "La posicion esta vacia"

class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"
    
class KingCaptureNotAllowed(InvalidMove):
    message = "No esta permitido capturar al rey"
    def __str__(self):
        return self.message
    
    

    
#guardado en raise es opcional no es un requisito obligatorio