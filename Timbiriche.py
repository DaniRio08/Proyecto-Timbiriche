from colorama import init, Fore
init()
import random

# Esta porción de código pide a los jugadores una inicial para identificarse. Luego de forma aleatoria se establece
# quién jugará el primer turno
print()
Inicial_J1 = input("JUGADOR 1, ¿con que letra te quieres identificar? ")
while len(Inicial_J1) > 1:
    print("Es demasiado largo, solo puede ser una letra.")
    Inicial_J1 = input("Vuelve a introducir la letra con la que te quieres identificar: ")
print()
Inicial_J2 = input("JUGADOR 2, ¿con que letra te quieres identificar? ")
while len(Inicial_J2) > 1:
    print("Es demasiado largo, solo puede ser una letra.")
    Inicial_J2 = input("Vuelve a introducir la letra con la que te quieres identificar: ")
print()
turno = random.choice([Inicial_J1,Inicial_J2])
if turno == Inicial_J1:
    print(f"Empieza jugando el JUGADOR 1 ({Inicial_J1})")
elif turno == Inicial_J2:
    print(f"Empieza jugando el JUGADOR 2 ({Inicial_J2})")
print()
print("-------------------------------------------------------")
print()

# Variables para contar los puntos de cada jugador
puntos_J1 = 0
puntos_J2 = 0

partida_finalizada = False

# Funciones que verifican si se ha formado un cuadrado al introducir una línea horizontal.
def verificar_cuadrado_bajo(x,y,casillero):
    if casillero[y-1][x] != " " and casillero[y+1][x] != " " and casillero[y][x-2] != " " and casillero[y][x+2] != " ":
        return True
    else:
        return False

def verificar_cuadrado_arriba(x,y,casillero):
    if casillero[y-1][x] != " " and casillero[y+1][x] != " " and casillero[y][x-2] != " " and casillero[y][x+2] != " ":
        return True
    else:
        return False

# Funciones que verifican si se ha formado un cuadrado al introducir una línea vertical.
def verificar_cuadrado_izda(x,y,casillero):
    if casillero[y-1][x] != " " and casillero[y+1][x] != " " and casillero[y][x-2] != " " and casillero[y][x+2] != " ":
        return True
    else:
        return False

def verificar_cuadrado_dcha(x,y,casillero):
    if casillero[y-1][x] != " " and casillero[y+1][x] != " " and casillero[y][x-2] != " " and casillero[y][x+2] != " ":
        return True
    else:
        return False
def imprimir_casillero(casillero):
    for x in range (len(casillero)):
        for j in range (len(casillero[x])):
            print(casillero[x][j],end="")
        print()
#Creación de una matriz de casilleros vacíos 
casillero = [["+"," "," "," ","+"," "," "," ","+"," "," "," ","+"," "," "," ","+"],
             [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
             ["+"," "," "," ","+"," "," "," ","+"," "," "," ","+"," "," "," ","+"],
             [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
             ["+"," "," "," ","+"," "," "," ","+"," "," "," ","+"," "," "," ","+"],
             [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
             ["+"," "," "," ","+"," "," "," ","+"," "," "," ","+"," "," "," ","+"],
             [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
             ["+"," "," "," ","+"," "," "," ","+"," "," "," ","+"," "," "," ","+"]]

#Luego, utiliza un ciclo "for" anidado para imprimir cada elemento de la lista en una nueva línea.
imprimir_casillero(casillero)


# Bucle que dibuja la línea que quiere el jugador y vuelve a pedir coordenadas mientras la partida no se haya finalizado
while partida_finalizada == False:
    # Turno del Jugador1
    if turno == Inicial_J1:
        print()
        print(f"Turno JUGADOR 1 ({Inicial_J1})")
        print()
        x1, y1 = input("Introduce las coordenadas del primer punto x y: ").split()
        x2, y2 = input("Introduce las coordenadas del segundo punto x y: ").split()
        print()
        # Línea horizontal de izquierda a derecha
        if int(y1)==int(y2) and int(x1) + 1 == int(x2):
            casillero[int(y1)*2][int(x1)*4+1:4*int(x2)]=[Fore.BLUE+"-","-","-"+Fore.RESET]
            print()    

            # Nuevas coordenadas que representan el punto central del cuadrado de arriba y el de abajo que se usan para verificar 
            # si se ha cerrado un cuadrado
            xb = int(x1)*4+2
            yb = int(y1)*2+1
            xa = int(x1)*4+2
            ya = int(y1)*2-1
            
            # Cada línea puede cerrar dos cuadrados, excepto las que se situan en los bordes del tablero. Si no se hace esta excepción
            # surgen errores que no dejan continuar la partida
            if int(y1) == 0:
                if verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    imprimir_casillero(casillero)
                    turno = Inicial_J2

            elif int(y1) == 4:
                if verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    imprimir_casillero(casillero)
                    turno = Inicial_J2

            else :
                # Este condicional evalua si se han cerrado dos cuadrados a la vez. Si no se incluye, al cerrar dos cuadrados
                # simultanemente solo cuenta únicamente como uno cerrado
                if (verificar_cuadrado_bajo(xb, yb, casillero) == True) and (verificar_cuadrado_arriba(xa, ya, casillero) == True):
                    casillero[yb][xb]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    casillero[ya][xa]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido dos puntos!")
                    puntos_J1+=2
                    turno = Inicial_J1
                elif verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                elif verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J2

        # Línea horizontal de derecha a izquierda
        elif int(y1)==int(y2) and int(x1) - 1 == int(x2):
            casillero[int(y1)*2][int(x2)*4+1:4*int(x1)]=[Fore.BLUE+"-","-","-"+Fore.RESET]
            print()

            xb = int(x2)*4+2
            yb = int(y1)*2+1
            xa = int(x2)*4+2
            ya = int(y1)*2-1

            if int(y1) == 0:
                if verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J2

            elif int(y1) == 4:
                if verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J2

            else :
                if (verificar_cuadrado_bajo(xb, yb, casillero) == True) and (verificar_cuadrado_arriba(xa, ya, casillero) == True):
                    casillero[yb][xb]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    casillero[ya][xa]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido dos puntos!")
                    puntos_J1+=2
                    turno = Inicial_J1
                elif verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                elif verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J2
        
        # Líneas verticales
        elif (int(x1)==int(x2) and int(y1) + 1 == int(y2)) or (int(x1)==int(x2) and int(y1) - 1 == int(y2)):
            casillero[int(y1)+int(y2)][int(x1)*4]= Fore.BLUE+"|"+Fore.RESET
            print()

            xi = int(x1)*4-2
            yi = int(y1) + int(y2)
            xd = int(x1)*4+2
            yd = int(y1) + int(y2)

            if int(x1) == 0:
                if verificar_cuadrado_dcha(xd,yd,casillero) == True:
                    casillero[yd][xd]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J2

            elif int(x1) == 4:
                if verificar_cuadrado_izda(xi,yi,casillero) == True:
                    casillero[yi][xi]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J2

            else: 
                if (verificar_cuadrado_dcha(xd,yd,casillero) == True) and (verificar_cuadrado_izda(xi,yi,casillero) == True):
                    casillero[yd][xd]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    casillero[yi][xi]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido dos puntos!")
                    puntos_J1+=2
                    turno = Inicial_J1
                elif verificar_cuadrado_dcha(xd,yd,casillero) == True:
                    casillero[yd][xd]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                elif verificar_cuadrado_izda(xi,yi,casillero) == True:
                    casillero[yi][xi]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J2

            if puntos_J1 + puntos_J2 == 16:
                partida_finalizada = True

        print()
        print(Fore.YELLOW+"--------MARCADOR--------"+Fore.RESET)
        print()
        print(f"JUGADOR 1: {puntos_J1} puntos.")
        print(f"JUGADOR 2: {puntos_J2} puntos.")
        print()
        print(Fore.YELLOW+"--------MARCADOR--------"+Fore.RESET)
        print()

    elif turno == Inicial_J2:
        print()
        print(f"Turno JUGADOR 2 ({Inicial_J2})")
        print()
        x1, y1 = input("Introduce las coordenadas del primer punto x y: ").split()
        x2, y2 = input("Introduce las coordenadas del segundo punto x y: ").split()
        print()
        # Línea horizontal de izquierda a derecha
        if int(y1)==int(y2) and int(x1) + 1 == int(x2):
            casillero[int(y1)*2][int(x1)*4+1:4*int(x2)]=[Fore.RED+"-","-","-"+Fore.RESET]
            print()

            xb = int(x1)*4+2
            yb = int(y1)*2+1
            xa = int(x1)*4+2
            ya = int(y1)*2-1
            
            if int(y1) == 0:
                if verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J2+=1
                    turno = Inicial_J2
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J1

            elif int(y1) == 4:
                if verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J2+=1
                    turno = Inicial_J2
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J1

            else :
                if (verificar_cuadrado_bajo(xb, yb, casillero) == True) and (verificar_cuadrado_arriba(xa, ya, casillero) == True):
                    casillero[yb][xb]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    casillero[ya][xa]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido dos puntos!")
                    puntos_J2+=2
                    turno = Inicial_J2
                elif verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J2+=1
                    turno = Inicial_J2
                elif verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J2+=1
                    turno = Inicial_J2
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J1

        # Línea horizontal de derecha a izquierda
        elif int(y1)==int(y2) and int(x1) - 1 == int(x2):
            casillero[int(y1)*2][int(x2)*4+1:4*int(x1)]=[Fore.RED+"-","-","-"+Fore.RESET]
            print()

            xb = int(x2)*4+2
            yb = int(y1)*2+1
            xa = int(x2)*4+2
            ya = int(y1)*2-1

            if int(y1) == 0:
                if verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J2+=1
                    turno = Inicial_J2
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J1

            elif int(y1) == 4:
                if verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J2+=1
                    turno = Inicial_J2
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J1

            else :
                if (verificar_cuadrado_bajo(xb, yb, casillero) == True) and (verificar_cuadrado_arriba(xa, ya, casillero) == True):
                    casillero[yb][xb]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    casillero[ya][xa]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido dos puntos!")
                    puntos_J2+=2
                    turno = Inicial_J2
                elif verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J2+=1
                    turno = Inicial_J2
                elif verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J2+=1
                    turno = Inicial_J2
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J1
        
        # Líneas verticales
        elif (int(x1)==int(x2) and int(y1) + 1 == int(y2)) or (int(x1)==int(x2) and int(y1) - 1 == int(y2)):
            casillero[int(y1)+int(y2)][int(x1)*4]= Fore.RED+"|"+Fore.RESET
            print()

            xi = int(x1)*4-2
            yi = int(y1) + int(y2)
            xd = int(x1)*4+2
            yd = int(y1) + int(y2)

            if int(x1) == 0:
                if verificar_cuadrado_dcha(xd,yd,casillero) == True:
                    casillero[yd][xd]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J2+=1
                    turno = Inicial_J2
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J1

            elif int(x1) == 4:
                if verificar_cuadrado_izda(xi,yi,casillero) == True:
                    casillero[yi][xi]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J2+=1
                    turno = Inicial_J2
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J1

            else:
                if (verificar_cuadrado_dcha(xd,yd,casillero) == True) and (verificar_cuadrado_izda(xi,yi,casillero) == True):
                    casillero[yd][xd]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    casillero[yi][xi]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido dos puntos!")
                    puntos_J2+=2
                    turno = Inicial_J2         
                elif verificar_cuadrado_dcha(xd,yd,casillero) == True:
                    casillero[yd][xd]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J2+=1
                    turno = Inicial_J2
                elif verificar_cuadrado_izda(xi,yi,casillero) == True:
                    casillero[yi][xi]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J2+=1
                    turno = Inicial_J2
                else:
                    imprimir_casillero(casillero)
                    print()
                    turno = Inicial_J1
            if puntos_J1 + puntos_J2 == 16:
                partida_finalizada = True

        print()
        print(Fore.YELLOW+"--------MARCADOR--------"+Fore.RESET)
        print()
        print(f"JUGADOR 1: {puntos_J1} puntos.")
        print(f"JUGADOR 2: {puntos_J2} puntos.")
        print()
        print(Fore.YELLOW+"--------MARCADOR--------"+Fore.RESET)
        print()

if puntos_J1 > puntos_J2 :
    print(f"¡EL JUGADOR 1 ({Inicial_J1}) HA GANADO LA PARTIDA!")
elif puntos_J2 > puntos_J1 :
    print(f"¡EL JUGADOR 2 ({Inicial_J2}) HA GANADO LA PARTIDA!")
else:
    print("LA PARTIDA HA ACABADO EN EMPATE")