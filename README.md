# ♘♕ Ajedrez - OOP en Python ♕♘
*Marina Lucila Rivadeneira*
*63267*

# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-mar1naRivadeneira/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-mar1naRivadeneira/tree/main)

# Maintainability 
[![Maintainability](https://api.codeclimate.com/v1/badges/fd901bfd7f32f49569e7/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-mar1naRivadeneira/maintainability)

# Test Coverage 
[![Test Coverage](https://api.codeclimate.com/v1/badges/fd901bfd7f32f49569e7/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-mar1naRivadeneira/test_coverage)

# ♟️ Descripción

Este proyecto implementa un juego de ajedrez básico en Python, diseñado con un enfoque orientado a objetos. Incluye los movimientos esenciales de todas las piezas, pero no contempla reglas avanzadas como jaque, jaque mate, enroque o captura al paso. El juego finaliza cuando un jugador elimina todas las piezas de su oponente o cuando ambos deciden terminar la partida.

## ⚙️ Requisitos

- *Python 3.x*
- *Docker*
- *Instalar las dependencias*

## 🔍 Características

- *Tablero*: Un tablero de 8x8 que refleja la disposición inicial clásica de las piezas.
- *Piezas*: Cada tipo de pieza (Rey, Reina, Torre, Alfil, Caballo, Peón) tiene su propia clase y comportamiento.
- *Reglas de Movimiento*: Se valida que cada pieza siga sus movimientos correctos, con capturas y restricciones.
- *CLI*: El juego se controla a través de comandos en la consola.
- *Finalización del juego*: La partida termina cuando un jugador pierde todas sus piezas o si ambos deciden finalizarla, escribiendo "fin" en la consola.
- *Pruebas*: Hay pruebas unitarias para asegurar que las piezas y las reglas funcionen correctamente.
- *Soporte Docker*: Se puede ejecutar y probar el juego en un entorno Dockerizado.

## 🚀 Instrucciones de Uso

1. Clona el repositorio:

   https://github.com/um-computacion-tm/ajedrez-2024-mar1naRivadeneira.git

2. Instala las dependencias:

   pip install -r requirements.txt

3. Ejecuta el juego:

   python3 -m chess.cli

## 🐳 Docker

1. Crear imagen Docker:

   docker buildx build -t ajedrez-2024-mar1naRivadeneira .

2. Ejecutar el contenido y correr tests:

   docker run -i ajedrez-2024-mar1naRivadeneira
