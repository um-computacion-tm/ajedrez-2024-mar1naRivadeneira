from chess.ajedrez import Chess            
from chess.excepciones import InvalidMove, InvalidTurn, EmptyPosition, SamePosition, OutOfBoard
#aca se pide coordenadas o cuando quiere terminar la partida el usuario pero solo llama las funciones que estan en el chess
def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)

def play(chess):
    try:

        print(chess.show_board())
        print("turn: ", chess.turn) 
        print("Ingresa coordenadas o fin para terminar la partida: ")
        
        def get_input_or_end(prompt):
            command = input(prompt).lower()
            if command == "fin":                                                  
                chess.end_by_agreement()
                print("Los jugadores decidieron finalizar la partida. ¡Gracias por jugar!")
                raise SystemExit  #para salir del juego
            return int(command)  #si no es fin convierte a entero
        
        from_row = get_input_or_end("From row: ")
        from_col = get_input_or_end("From col: ")
        to_row = get_input_or_end("To Row: ")
        to_col = get_input_or_end("To Col: ")
            
         # :) solo se ejecuta si el ingreso es bueno, si esta mal no se ejecuta el move
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

    except InvalidMove as e:
        print("Movimiento invalido. Por favor, revisa las reglas y asegurate de hacer movimientos permitidos.")   #el orden de las excepciones importa,  tiene que ir de la mas particular a la mas general
        
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}") 
            
if __name__ == '__main__':
    main()