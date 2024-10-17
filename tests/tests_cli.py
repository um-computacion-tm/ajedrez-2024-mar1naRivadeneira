import unittest
from unittest.mock import patch, MagicMock
from chess.ajedrez import Chess
from chess.cli import play      #patch sobreescribe el comportamiento de algo, en este caso sobreescribe el print, el imput no se ejecuta
from chess.excepciones import (InvalidMove, InvalidTurn, EmptyPosition, SamePosition, OutOfBoard, SameColorCapture)

class TestCli(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()
        
    @patch(
        'builtins.input',
        side_effect=['1', '1', '2', '2'],
    )                                                  
    @patch('builtins.print') 
    @patch.object(Chess, 'move')
    def test_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): 
        """
        Prueba el flujo normal donde el usuario ingresa coordenadas validas
        """
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 1)
        
    @patch( 
        'builtins.input',
        side_effect=['hola', '1', '2', '2'],
    )
    
    @patch('builtins.print') 
    @patch.object(Chess, 'move')

    def test_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): 
        """Prueba cuando el jugador ingresa una entrada no valida(no numerica)"""
        
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 4)
        self.assertEqual(mock_chess_move.call_count, 0)    
        
    @patch( 
        'builtins.input',
        side_effect=['1', '1', '2', 'hola'], 
    )

    @patch('builtins.print') 
    @patch.object(Chess, 'move')
    
    def test_more_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): 
        """Prueba cuando una de las coordenadas no es valida (no numerica)"""
        
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 4)
        self.assertEqual(mock_chess_move.call_count, 0)    
        
    @patch('builtins.input', side_effect=['1', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_invalid_move_exception(
        self,
        mock_chess_move,
        mock_print,
        mock_input
    ):
        """
        Prueba cuando se lanza la excepción InvalidMove.
        """
        mock_chess_move.side_effect = InvalidMove()

        play(self.chess)

        mock_print.assert_any_call("Movimiento invalido. Por favor, revisa las reglas y asegurate de hacer movimientos permitidos.")

    @patch('builtins.input', side_effect=['1', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_invalid_turn_exception(
        self,
        mock_chess_move,
        mock_print,
        mock_input
    ):
        """
        Prueba cuando se lanza la excepción InvalidTurn.
        """
        mock_chess_move.side_effect = InvalidTurn()

        play(self.chess)

        mock_print.assert_any_call("Es el turno de tu oponente. Espera tu turno para mover tus piezas.")

    @patch('builtins.input', side_effect=['1', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_empty_position_exception(
        self,
        mock_chess_move,
        mock_print,
        mock_input
    ):
        """
        Prueba cuando se lanza la excepción EmptyPosition.
        """
        mock_chess_move.side_effect = EmptyPosition()

        play(self.chess)

        mock_print.assert_any_call("No hay ninguna pieza en la posición de origen.")

    @patch('builtins.input', side_effect=['1', '1', '1', '1'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_same_position_exception(
        self,
        mock_chess_move,
        mock_print,
        mock_input
    ):
        """
        Prueba cuando se lanza la excepción SamePosition.
        """
        mock_chess_move.side_effect = SamePosition()

        play(self.chess)

        mock_print.assert_any_call("No se puede mover la pieza a la misma direccion de origen.")

    @patch('builtins.input', side_effect=['8', '8', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_out_of_board_exception(
        self,
        mock_chess_move,
        mock_print,
        mock_input
    ):
        """
        Prueba cuando se lanza la excepción OutOfBoard.
        """
        mock_chess_move.side_effect = OutOfBoard()

        play(self.chess)

        mock_print.assert_any_call("Las coordenadas están fuera del tablero. Intenta de nuevo con valores de 0 al 7.")

    @patch('builtins.input', side_effect=['1', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_value_error_exception(
        self,
        mock_chess_move,
        mock_print,
        mock_input
    ):
        """
        Prueba cuando se lanza una excepción ValueError.
        """
        mock_chess_move.side_effect = ValueError()

        play(self.chess)

        mock_print.assert_any_call("Entrada invalida. Por favor, ingrese numeros para las coordenadas.")

    @patch('builtins.input', side_effect=['1', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_unexpected_exception(
        self,
        mock_chess_move,
        mock_print,
        mock_input
    ):
        """
        Prueba cuando se lanza una excepción inesperada.
        """
        mock_chess_move.side_effect = Exception("Error desconocido")

        play(self.chess)

        mock_print.assert_any_call("Ocurrio un error inesperado: Error desconocido")

    @patch('builtins.input', side_effect=['fin'])
    @patch('builtins.print')
    def test_end_by_agreement(
        self,
        mock_print,
        mock_input
    ):
        """
        Prueba que el juego finaliza por acuerdo mutuo cuando el usuario ingresa 'fin'.
        """
        play(self.chess)

        mock_print.assert_any_call("Los jugadores decidieron finalizar la partida. ¡Gracias por jugar!")
        self.assertFalse(self.chess.is_playing())

    ### Pruebas Adicionales para Completar Cobertura ###

    @patch('builtins.input', side_effect=['1', '1', '1', '1'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_move_to_same_position_no_exception(
        self,
        mock_chess_move,
        mock_print,
        mock_input
    ):
        """
        Prueba que intentar mover a la misma posición lanza la excepción SamePosition y no cambia el estado del juego.
        """
        mock_chess_move.side_effect = SamePosition()

        play(self.chess)

        mock_print.assert_any_call("No se puede mover la pieza a la misma direccion de origen.")
        self.assertTrue(self.chess.is_playing())

if __name__ == '__main__':
    unittest.main()                