from chess.ajedrez import Chess            #jeraquia de invalidmove de rook,piece,pawn pero todas son movimientos invalidos pero algunas especificos
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
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))
            
         # :) solo se ejecuta si el ingreso es bueno, si esta mal no se ejecuta el move
        chess.move(              
            from_row,            
            from_col,
            to_row,
            to_col,
        )
    
    except OutOfBoard as e:
        print("Las coordenadas están fuera del tablero.")    
            
    except EmptyPosition as e:
        print("No hay ninguna pieza en la posición de origen.")
                
    except SamePosition as e:
        print("No se puede mover la pieza a la misma direccion de origen")
        
    except InvalidTurn as e:
        print("Es el turno del oponente.")    

    except InvalidMove as e:
        print("Su movimiento es invalido")   #el orden de las excepciones importa,  tiene que ir de la mas particular a la mas general
        
    except Exception as e:
        print("error", e) 
            
if __name__ == '__main__':
    main()