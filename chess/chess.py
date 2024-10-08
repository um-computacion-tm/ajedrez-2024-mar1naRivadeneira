from chess.board import Board
from chess.excepciones import InvalidMove, InvalidTurn, EmptyPosition, KingCaptureNotAllowed
from chess.king import King

class Chess:
    def __init__(self, for_test = False):
        self.__turn__ = "WHITE"
        self.__board__ = Board()
        
        
    def is_playing(self):
        return True

    def move( self, from_row, from_col, to_row, to_col, ):
        #validacion de coordenadas
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece :
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        if not piece.get_valid_moves(from_row, from_col, to_row, to_col):
            raise InvalidMove() #generaliza el movimiento invalido para todas las piezas
        
        destination_piece = self.__board__.get_piece( to_row, to_col)
        if isinstance(destination_piece, King):
            raise KingCaptureNotAllowed()#no se puede permitir capturar al rey
        
        
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()    
        
   
    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"