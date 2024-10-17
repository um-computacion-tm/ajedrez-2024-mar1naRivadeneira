from chess.board import Board
from chess.excepciones import InvalidMove, InvalidTurn, EmptyPosition, SamePosition, SameColorCapture

class Chess:
    def __init__(self, for_test = False):
        """Inicializa una nueva partida de ajedrez.
        Args:
            for_test (bool): Si es True, inicializa el tablero sin piezas para pruebas."""
        self.__turn__ = "WHITE"
        self.__board__ = Board()
        self.__playing__ = True #Indica si el juego sigue en curso
        
    def is_playing(self):
        """Verifica si el juego sigue en curso.
        Returns:
            bool: True si el juego está activo, False de lo contrario."""
        return self.__playing__

    def move( self, from_row, from_col, to_row, to_col):
        """Realiza un movimiento de una pieza en el tablero.
        
        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.
        
        Raises:
            Exception: Si el juego ha terminado.
            EmptyPosition: Si no hay ninguna pieza en la posición de origen.
            InvalidTurn: Si no es el turno del color de la pieza seleccionada.
            SamePosition: Si la posición de origen y destino son las mismas.
            SameColorCapture: Si se intenta capturar una pieza del mismo color.
            InvalidMove: Si el movimiento no es válido según las reglas de la pieza."""
        if not self.__playing__:
            raise Exception("el juego ha terminado.")
        
        piece = self.__board__.get_piece(from_row, from_col)
        
        if not piece :
            raise EmptyPosition()
        
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        
        if from_row == to_row and from_col == to_col:
            raise SamePosition()
    
        destination_piece = self.__board__.get_piece( to_row, to_col)
        
        if destination_piece is not None and destination_piece.get_color() == piece.get_color():
            raise SameColorCapture() 
        
        if not piece.get_valid_moves(from_row, from_col, to_row, to_col):
            raise InvalidMove() 
        
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()    
   
    def check_end_game(self):
        """Verifica si algún jugador ha quedado sin piezas, determinando así el ganador.
        Returns:
            str or None: El color del ganador ("WHITE" o "BLACK") si hay uno, o None si no."""
        if not self.__board__.has_pieces("WHITE"):
            self.__playing__ = False
            return "BLACK"
        elif not self.__board__.has_pieces("BLACK"):
            self.__playing__ = False
            return "WHITE"
        return None 
    
    def end_by_agreement(self):
        """Finaliza el juego por acuerdo mutuo entre los jugadores."""
        self.__playing__ = False
        
    @property
    def turn(self):
        """Obtiene el color del jugador cuyo turno es actualmente.
        Returns:
            str: "WHITE" o "BLACK" indicando el turno actual."""
        return self.__turn__

    def show_board(self):
        """Obtiene una representación en cadena del estado actual del tablero.
        Returns:
            str: Representación del tablero."""
        return str(self.__board__)
    
    def change_turn(self):
        """ Cambia el turno al siguiente jugador."""
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"