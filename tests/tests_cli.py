import unittest
from unittest.mock import patch
from chess.chess import Chess
from chess.cli import play      #patch sobreescribe el comportamiento de algo, en este caso sobreescribe el print, el imput no se ejecuta


class TestCli(unittest.TestCase):
    @patch(# este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', '2'],# estos son los valores que simula lo que ingresaria el usuario
    )                                                  
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    def test_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #

        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 1)
        
    @patch( # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['hola', '1', '2', '2'],
    )
    
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')

    def test_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #

        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 0)    
        
    @patch( # este patch controla lo que hace el input 
        'builtins.input',
        side_effect=['1', '1', '2', 'hola'], 
    )

    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    
    def test_more_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #

        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 0)    
        
if __name__ == '__main__':
    unittest.main()                