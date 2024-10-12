# Changelog

## [0.1] - 23 / 08 / 2024

## Agregado
- Agregado de posiciones en el board
- Creacion de las piezas
- Agregado de turnos
- tests de turno, cli y board
- movimientos en vertical de pawn y rook

## [0.2] - 01 / 09 / 2024

## Agregado
- agregado del test de show_board en la clase chess
- arreglo en el color de las piezas
- agregado del movimiento descendente y ascendente de la pieza rook
- test de los movimiento desc y asc de rook
- agregado del metodo set_ piece y __str__

## [0.3] - 03 / 09 / 2024

## Agregado

- agregado de test_move para verificar el movimiento de la torre en el tablero
- agregado del test get_piece
- actualizacion del metodo move en la clase Board

## [0.4] - 08 / 09 / 2024

## Agregado
- agregado de excepciones
- test piezas fuera del rango del tablero
- arreglos en los colores de las piezas
- modificacion en el metodo move
- testeo de las excepciones InvalidMove e InvalidTurn del metodo move
- test del movimiento de rook
- agregado del movimiento horizontal del rook

## [0.5] - 19 / 09 / 2024

## Agregado

- agregado de movimientos diagonales del bishop
- test de movimientos diagonales ascendentes y descendentes de bishop
- test de movimientos horizontales de rook
- test de excepcion InvalidMove

## [0.6] - 25 / 09 / 2024

## Agregado

- agregado de metodo para verificar si hay una pieza en una posicion
- agregado de metodo para verificar si es una pieza enemiga la que esta en una posicion
- agregado de general_moves para evitar repeticion
- correccion de errores en rook y bishop 
- actualizacion de test de rook y bishop
- test de la excepcion OutOfBoard de board

## [0.7] - 28 / 09 / 2024

## Agregado

- agregado actualizacion del movimientos de piezas 
- correccion de issue cognitive complexity en pawn
- agregado metodo verify_promote y promote para promocion del peon

## [0.8] - 02 / 10 / 2024

## Agregado

- arreglo del double_step_move en peon 
- agregado de posiciones de rook y bishop en piece
- cambio en valid_position de rook y bishop 
- arreglo en los tests de rook y bishop
- arreglo en la verificacion de pieza enemiga en general_move en piece

## [0.9] - 12 / 10 / 2024

## Agregado

- mejora en la actualizacion del tablero 
- agregado de mensaje de las excepciones en cli 
- actualizacion de los test
- agregado excepcion sameposition
- agregado tests de movimientos del rey
- agregado tests de movimientos de la reina
- arreglos en los movimientos de la reina y rey para evitar duplicacion
