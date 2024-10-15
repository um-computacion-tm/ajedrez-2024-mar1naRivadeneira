from chess.board import Board
from chess.excepciones import InvalidMove, InvalidTurn, EmptyPosition, SamePosition

class Chess:
    def __init__(self, for_test = False):
        self.__turn__ = "WHITE"
        self.__board__ = Board()
        self.__playing__ = True #Indica si el juego sigue en curso
        
    def is_playing(self):
        return self.__playing__

    def move( self, from_row, from_col, to_row, to_col):
        if not self.__playing__:
            raise Exception("el juego ha terminado.")
        
        #validacion de coordenadas
        piece = self.__board__.get_piece(from_row, from_col)
        
        if not piece :
            raise EmptyPosition()
        
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        
        if not piece.get_valid_moves(from_row, from_col, to_row, to_col):
            raise InvalidMove() #generaliza el movimiento invalido para todas las piezas
        
        destination_piece = self.__board__.get_piece( to_row, to_col)
        
        if from_row == to_row and from_col == to_col:
            raise SamePosition()# excepcion para que no se mueva una pieza a a la misma posicion
        
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()    
   
    
    
    #Finaliza el juego por acuerdo mutuo entre los jugadores
    def end_by_agreement(self):
        self.__playing__ = False
        
    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)
    
    #Cambia el turno entre WHITE y BLACK
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"