

import os
import random
from re import X
from tkinter import Y


def crea_tablero(fil, col, val):
    # Crea una matriz con las filas y columnas y valor que le pasemos
    
    tablero = []
    for i in range(fil):
        tablero.append([])
        for j in range(col):
            tablero[i].append(val)
    return tablero

def muestra_tablero(tablero):
    # Muestra en filas y columnas la matriz que le pasemos
    print("******************************************* ")
    for fila in tablero:
        print("*", end="")
        for elem in fila:
            print(elem, end=" ")
        print("*")
    print("******************************************* ")




# Generamos una matriz de minas

def coloca_minas(tablero, minas, fil, col):
    
    #Coloca en el tablero que le pasemos el numero de minas que le pasemos
    
    minas_ocultas = []    
    numero = 0
    while numero < minas:
        y = random.randint(0, fil - 1)
        x = random.randint(0, col - 1)
        if tablero[y][x] != 9:
            tablero[y][x] = 9
            numero += 1   
            minas_ocultas.append([y, x])

    return tablero, minas_ocultas

def coloca_pistas(tablero, fil, col):
    
    for y in range(fil):
        for x in range(col):
            if tablero[y][x] == 9:
                for i in [-1, 0 ,1]:
                    for j in [-1, 0, 1]:
                        if 0 <= y + i < fil - 1 and 0 <= x + j < col - 1:
                            if tablero[y+i][x+j] != 9:
                                tablero[y+i][x+j] += 1
                        
    return tablero                

def tablero_completo(tablero, fil, col, val):
    '''Comprueba si el tablero no tiene ningina casilla con el valor visible inicial'''
    for y in range(fil):
        for x in range(col):
            if tablero[y][x] == val:
                return False
    return True
        
# Presentacion

def presentacion():
    
    '''Pantalla de presentacion'''

    os.system("clear")
    
    print("************************")
    print("*    JUEGO MINESWEEPER   *")
    print("************************")
    print("* w/a/s/d = moverse    *")
    print("* m = mostrar            *")
    print("* q = salir            *")
    print("*     b/v - marcar/desmarcar")
    print()
    print("Enter para empezar")


def menu():
    '''Devuelve el movimiento y opcion elegida por el usuario'''
    print()
    opcion = input("w/a/s/d/m/q/b/v: ")
    return opcion

def rellenado (oculto, visible, y, x , fil, col, val):
    '''Recorre todas las casillas vecinas y comprueba si son ceros, si es asi las descubre y recorre las
    vecinas dee estas, hasta encontrar casillas con pistas, que tambien descubre.'''

    ceros = [(y,x)]

    while len(ceros) > 0:
        y , x = ceros.pop()
        for i in [-1, 0 ,1]:
            for j in [-1, 0, 1]:
                if 0 <= y + i < fil - 1 and 0 <= x + j <= col - 1:
                    if visible[y+i][x+j] == val and oculto[y+i][x+j] == 0:
                        visible[y+i][x+j] = 0
                        if(y+i, x+j) not in ceros:
                            ceros.append((y+i, x+j))
                        else:
                            visible[y+i][x+j] = oculto[y+i][x+j] 

    return visible

def reemplaza_ceros(tablero):
    for i in range(12):
        for j in range(16):
            if tablero[i][j] == 0:
                tablero[i][j] = " "
                
#### Flujo del programa


columnas = 16
filas = 12

visible = crea_tablero(filas, columnas, "-")

oculto  = crea_tablero(filas, columnas, 0)

oculto, minas_ocultas = coloca_minas(oculto, 15, filas, columnas)

oculto = coloca_pistas(oculto, filas, columnas)

presentacion()

# Colocamos ficha inicial y mostramos tablero

y = random.randint(2, filas - 3)
x = random.randint(2, columnas - 3)

real = visible[y][x]
visible[y][x] = "x"

os.system("clear")

muestra_tablero(visible)



#Bucle principal

minas_marcadas = []

jugando = True

while jugando:
    mov = menu()

    if mov == "w":
        if y == 0:
            y -= 1
        else:
            visible[y][x] = real
            y -= 1
            real = visible[y][x]
            visible[y][x] = "x"
        
    elif mov == "s":
        if y == filas - 1:
            y = filas - 1
        else:
            visible[y][x] = real
            y += 1
            real = visible[y][x]
            visible[y][x] = "x"
    
    elif mov == "a":
        if x == 0:
            x = 0
        else:
            visible[y][x] = real
            x -= 1
            real = visible[y][x]
            visible[y][x] = "x"
    
    elif mov == "d":
        if x == columnas - 1:
            x = columnas - 1
        else:
            visible[y][x] = real
            x += 1
            real = visible[y][x]
            visible[y][x] = "x"
            
    elif mov == "b":
        if real == "-":
            visible[y][x] = "#"
            real = visible[y][x]
            if (y, x) not in minas_marcadas:
                minas_marcadas.append((y, x))
    
    elif mov == "v":
        if real == "#":
            visible[y][x] = "-"
            real = visible[y][x]
            if (y, x) in minas_marcadas:
                minas_marcadas.remove((y, x))
                
    elif mov == "m":
        if oculto[y][x] == 9:
            visible[x][y] = "@"
            jugando = False
            print("Has perdido")

        elif oculto [y][x] != 0:
            visible[y][x] = oculto[y][x]
            real = visible[y][x]
            
        elif oculto[y][x] == 0:
            visible[y][x] = 0
            visible = rellenado(oculto, visible, y, x, filas, columnas, '-')
            visible = reemplaza_ceros(visible)
            real = visible[y][x]

    os.system("clear")
    
    muestra_tablero(visible)
    
    ganas = False
    
    if tablero_completo( visible, filas , columnas, "-") and \
        sorted(minas_marcadas) == sorted(minas_ocultas) and \
        real != '-':
        ganas = True
        jugando = False
        
        
    if not ganas:
        print("Has perdido")
    else:
        print("Has ganado")