from chess.ajedrez import Chess            
from chess.excepciones import InvalidMove, InvalidTurn, EmptyPosition, SamePosition, OutOfBoard, SameColorCapture

def main():
    """Punto de entrada principal para la interfaz de línea de comandos del juego de ajedrez."""
    chess = Chess()
    while chess.is_playing():
        play(chess)

def play(chess):
    """Maneja una ronda de juego, solicitando y procesando la entrada del usuario.
    Args:
        chess (Chess): Instancia actual del juego de ajedrez."""
    try:

        print(chess.show_board())
        print("turn: ", chess.turn) 
        print("Ingresa coordenadas o fin para terminar la partida: ")
        
        def get_input_or_end(prompt):
            """Obtiene la entrada del usuario o finaliza el juego si el usuario ingresa 'fin'.
            Args:
                prompt (str): Texto para mostrar al solicitar la entrada.
            Returns:
                int: Coordenada ingresada por el usuario.
            Raises:
                SystemExit: Para salir del juego si el usuario ingresa 'fin'."""
            command = input(prompt).lower()
            if command == "fin":                                                  
                chess.end_by_agreement()
                print("Los jugadores decidieron finalizar la partida. ¡Gracias por jugar!")
                raise SystemExit  
            return int(command)  
        
        from_row = get_input_or_end("From row: ")
        from_col = get_input_or_end("From col: ")
        to_row = get_input_or_end("To Row: ")
        to_col = get_input_or_end("To Col: ")
            
        chess.move(              
            from_row,            
            from_col,
            to_row,
            to_col,
        )
    
        winner = chess.check_end_game()
        if winner:
            print(f"El ganador es {winner}")
            print("¡Gracias por jugar!")
            
    except ValueError:
        print("Entrada invalida. Por favor, ingrese numeros para las coordenadas.")       
            
    except SystemExit:
        pass    
            
    except OutOfBoard as e:
        print("Las coordenadas están fuera del tablero. Intenta de nuevo con valores de 0 al 7.")    
            
    except EmptyPosition as e:
        print("No hay ninguna pieza en la posición de origen.")
                
    except SamePosition as e:
        print("No se puede mover la pieza a la misma direccion de origen.")
        
    except InvalidTurn as e:
        print(f"Es el turno de tu oponente. Espera tu turno para mover tus piezas.")    
        
    except SameColorCapture:
        print ("No puedes capturar piezas de tu mismo color. Intenta otro movimiento.")

    except InvalidMove as e:
        print("Movimiento invalido. Por favor, revisa las reglas y asegurate de hacer movimientos permitidos.")   
        
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}") 
            
if __name__ == '__main__':
    main()