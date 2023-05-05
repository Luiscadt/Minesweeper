## Minesweeper game in Python

This is a simple implementation of the classic Minesweeper game in Python. The game consists of a grid of cells, some of which contain hidden mines. The player must uncover all the cells that do not contain mines, by revealing the contents of each cell one at a time. If the player reveals a mine, the game is over.

The game is played using the following controls:
* w/a/s/d: move the cursor up/left/down/right
* m: reveal the contents of the current cell
* b/v: mark/unmark a cell as a mine
* q: quit the game

The game starts by presenting a grid of hidden cells. The player can move a cursor around the grid using the controls. When the player reveals the contents of a cell, one of the following happens:
* If the cell contains a mine, the game is over and the player loses.
* If the cell contains a number, that number is displayed in the cell, indicating the number of mines that are adjacent to the cell.
* If the cell is blank, all adjacent cells are automatically revealed, and the process repeats for each of these cells.

The game is won when all non-mine cells are revealed.

The code consists of several functions:
* `crea_tablero`: creates a grid of cells with the specified number of rows and columns, and initializes all cells to a specified value.
* `muestra_tablero`: prints the contents of the grid.
* `coloca_minas`: places a specified number of mines randomly on the grid.
* `coloca_pistas`: computes the number of mines adjacent to each cell, and stores that value in the cell.
* `rellenado`: recursively reveals all adjacent blank cells.
* `menu`: reads input from the user and returns the corresponding action.
* `presentacion`: prints the title screen.
* `reemplaza_ceros`: replaces all blank cells with spaces.

The main loop of the game reads input from the user, updates the state of the game accordingly, and prints the new state of the grid. The loop continues until the game is won, the game is lost, or the user quits.

## Juego de Minesweeper en Python

Este es un juego de Minesweeper implementado en Python. El objetivo del juego es encontrar todas las minas en el tablero sin hacer explotar ninguna de ellas. ¡Buena suerte!

## Instrucciones

Las teclas 'w', 'a', 's' y 'd' se utilizan para moverse por el tablero. La tecla 'm' muestra todo el tablero, la tecla 'q' sale del juego y las teclas 'b' y 'v' se utilizan para marcar y desmarcar las minas.

## Cómo jugar

En cada turno, seleccione una casilla del tablero. Si la casilla es una mina, pierdes el juego. Si la casilla no es una mina, se revelará un número que indica cuántas minas hay en las casillas adyacentes. Si todas las casillas que no son minas están descubiertas, ¡has ganado el juego!

## Código fuente

Puede encontrar el código fuente de este juego en Python en el archivo adjunto.

¡Diviértete jugando!
