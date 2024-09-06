from chess.board import Board
from chess.excepciones import InvalidMove, InvalidTurn, EmptyPosition


class Chess:
    def __init__(self):
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
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.__board__.move( from_row, from_col, to_col, to_row)
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