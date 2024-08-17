from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move( self, from_row, from_col, to_row, to_col, ):
        #validacion de coordenadas
        if not self.__is_valid_position(from_row, from_col):
            raise ValueError("posicion de origen invalida")
        if not self.__is_valid_position(to_row, to_col):
            raise ValueError("posicion de destino invalida")
        
        piece = self.__board__.get_piece(from_row, from_col)
        self.change_turn()
    
    def __is_valid_position(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
    
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"