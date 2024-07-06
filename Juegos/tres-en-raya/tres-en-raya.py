#Constantes
BLANCO = "⬜"
JUG1_FICH = "❌"
JUG2_FICH = "🔘"

def pintar_tablero(tablero: list) -> None:
    for i in range (3):
        for a in range (3):
            posi = tablero[i][a]
            if posi == 0:
                if a == 2:
                    print(f"{BLANCO}", end="  ")
                    print("\n")
                else:
                    print(f"{BLANCO}", end="  ")
            elif posi == 1:
                if a == 2:
                    print(f"{JUG1_FICH}", end="  ")
                    print("\n")
                else:
                    print(f"{JUG1_FICH}", end="  ")
            elif posi == 2:
                if a == 2:
                    print(f"{JUG2_FICH}", end="  ")
                    print("\n")
                else:
                    print(f"{JUG2_FICH}", end="  ")



def posiciones_libres(tablero: list) -> str:
    cont = 0
    pos = [0]
    for i in range (3):
        for a in range(3):
            cont += 1
            posi = tablero[i][a]
            if posi == 0:
                pos.append(cont)

    def listar_pos_libres(poss: list):
        for i in range(1,len(poss)):
            print(poss[i], end=", ")
            

    listar_pos_libres(pos)

    return pos



def pintar_tablero_jugador(jug: str, table: list) -> list:
    while True:
        posi = posiciones_libres(table)
        juga = int(input(f"{jug} que posicion quieres pintar??: "))
        if juga not in posi:
            print("Error")
        else:
            if juga == 1:
                if jug == "jugador1":
                    table[0][0] = 1
                    break
                else:
                    table[0][0] = 2
                    break
            elif juga == 2:
                    if jug == "jugador1":
                        table[0][1] = 1
                        break
                    else:
                        table[0][1] = 2
                        break
            elif juga == 3:
                    if jug == "jugador1":
                        table[0][2] = 1
                        break
                    else:
                        table[0][2] = 2
                        break
            elif juga == 4:
                    if jug == "jugador1":
                        table[1][0] = 1
                        break
                    else:
                        table[1][0] = 2
                        break
            elif juga == 5:
                    if jug == "jugador1":
                        table[1][1] = 1
                        break
                    else:
                        table[1][1] = 2
                        break
            elif juga == 6:
                    if jug == "jugador1":
                        table[1][2] = 1
                        break
                    else:
                        table[1][2] = 2
                        break
            elif juga == 7:
                    if jug == "jugador1":
                        table[2][0] = 1
                        break
                    else:
                        table[2][0] = 2
                        break
            elif juga == 8:
                    if jug == "jugador1":
                        table[2][1] = 1
                        break
                    else:
                        table[2][1] = 2
                        break
            elif juga == 9:
                    if jug == "jugador1":
                        table[2][2] = 1
                        break
                    else:
                        table[2][2] = 2
                        break
    return table

def comprobar_win(juga: int, tabl: list) ->bool:
    if (tabl[0][0] == juga) and (tabl [0][1] == juga) and (tabl[0][2] == juga):
        return True
    elif (tabl[1][0] == juga) and (tabl[1][1] == juga) and (tabl[1][2] == juga):
        return True
    elif (tabl[2][0] == juga) and (tabl[2][1] == juga) and (tabl[2][2]== juga):
        return True
    elif (tabl[0][0] == juga) and (tabl[1][0] == juga) and (tabl[2][0] == juga):
        return True
    elif (tabl[0][1] == juga) and (tabl[1][1] == juga) and (tabl[2][1] == juga):
        return True
    elif (tabl[0][2] == juga) and (tabl[1][2] == juga) and (tabl[2][2] == juga):
        return True
    elif (tabl[0][0] == juga) and (tabl[1][1] == juga) and (tabl[2][2] == juga):
        return True
    elif (tabl[0][2] == juga) and (tabl[1][1] == juga) and (tabl[2][0] == juga):
        return True
    else:
        False

def obtener_tablero_blanco() -> list:
    ta = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ] 
    return ta

def juego_ini():
    print("Bienvenidos al 3 en Raya!!!!!\nQue comience el juego.")
    tabl = obtener_tablero_blanco()
    pintar_tablero(tabl)

    while True:
        tabl=pintar_tablero_jugador("jugador1",tabl)
        if comprobar_win(1,tabl):
            print("El jugador 1 ha ganado!!!!")
            break
        pintar_tablero(tabl)
        tabl = pintar_tablero_jugador("jugador2",tabl)
        if comprobar_win(2,tabl):
            print("El jugador 2 ha ganado!!!!")
            break
        pintar_tablero(tabl)
    pintar_tablero(tabl)
juego_ini()