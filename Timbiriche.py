from colorama import init, Fore
init()
import random
import time
frase = Fore.LIGHTBLUE_EX+"BIENVENIDOS AL JUEGO DEL TIMBIRICHE TAMBIÉN CONOCIDO COMO EL JUEGO DE LOS CUADRADOS, SUERTE!!"+Fore.RESET

for letra in frase:
    print(letra, end="", flush=True)
    time.sleep(0.05)
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
n=int(input("Introduce el número de tamaño del casillero: "))
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
error_coordenadas = False
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
# Función para imprimir un casillero ,utiliza un ciclo "for" anidado para imprimir cada elemento de la lista en una nueva línea.
def imprimir_casillero(casillero):
    for x in range (len(casillero)):
        for j in range (len(casillero[x])):
            print(casillero[x][j],end="")
        print()
#Creación de una matriz de casilleros vacíos de tamaño variable
casillero = []
for i in range(n*2):
    fila = []
    for j in range(1+(n-1)*4):
        if i % 2 == 0:
            if j % 4 == 0:
                fila.append("+")
                if j==((n-1)*4):
                    fila.append(" "+str(i//2))
            else:
                fila.append(" ")
        elif i==(n*2-1):
            if j % 4 == 0:
                fila.append(str(j//4)+"   ")
        else:
            fila.append(" ")
    casillero.append(fila)

imprimir_casillero(casillero)


# Bucle que dibuja la línea que quiere el jugador y vuelve a pedir coordenadas mientras la partida no se haya finalizado
while partida_finalizada == False:
    # Turno del Jugador1
    if turno == Inicial_J1:
        if error_coordenadas == False:
            print()
            print(f"Turno JUGADOR 1 ({Inicial_J1})")
            print()
        error_coordenadas = False
        x1, y1 = map(int,input("Introduce las coordenadas del primer punto x y: ").split())
        x2, y2 = map(int,input("Introduce las coordenadas del segundo punto x y: ").split())
        print()
         # Bucle para evitar que sea posible introducir la misma línea dos veces
        while (((y1==y2 and x1 + 1 == x2) and (casillero[y1*2][x1*4+1:4*x2] != [" "," "," "]))
        or ((y1==y2 and x1 - 1 == x2) and (casillero[y1*2][x2*4+1:4*x1] != [" "," "," "]))
        or (((x1==x2 and y1 + 1 == y2) or (x1==x2 and y1 - 1 == y2)) and (casillero[y1+y2][x1*4] != " "))):
            print()
            print(Fore.RED+"ERROR: Esa línea ya ha sido dibujada, vuelve a intentarlo"+Fore.RESET)
            print()
            x1, y1 = map(int,input("Ingrese las coordenadas del primer punto x y: ").split())
            x2, y2 = map(int,input("Ingrese las coordenadas del segundo punto x y: ").split())
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

            elif int(y1) == n-1:
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

            elif int(y1) == n-1:
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

            elif int(x1) == n-1:
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
        else:
            print()
            print(Fore.RED+"ERROR: Esas coordenadas no son validas, vuelve a intentarlo"+Fore.RESET)
            print()
            error_coordenadas = True

        if puntos_J1 + puntos_J2 == (n-1)**2:
            partida_finalizada = True

        if error_coordenadas == False:
            print()
            print(Fore.YELLOW+"--------MARCADOR--------"+Fore.RESET)
            print()
            print(f"JUGADOR 1: {puntos_J1} puntos.")
            print(f"JUGADOR 2: {puntos_J2} puntos.")
            print()
            print(Fore.YELLOW+"--------MARCADOR--------"+Fore.RESET)
            print()

    elif turno == Inicial_J2:
        if error_coordenadas == False:
            print()
            print(f"Turno JUGADOR 1 ({Inicial_J1})")
            print()
        error_coordenadas = False
        x1, y1 = map(int,input("Introduce las coordenadas del primer punto x y: ").split())
        x2, y2 = map(int,input("Introduce las coordenadas del segundo punto x y: ").split())
        print()
        while (((y1==y2 and x1 + 1 == x2) and (casillero[y1*2][x1*4+1:4*x2] != [" "," "," "]))
        or ((y1==y2 and x1 - 1 == x2) and (casillero[y1*2][x2*4+1:4*x1] != [" "," "," "]))
        or (((x1==x2 and y1 + 1 == y2) or (x1==x2 and y1 - 1 == y2)) and (casillero[y1+y2][x1*4] != " "))):
            print()
            print(Fore.RED+"ERROR: Esa línea ya ha sido dibujada, vuelve a intentarlo"+Fore.RESET)
            print()
            x1, y1 = map(int,input("Ingrese las coordenadas del primer punto x y: ").split())
            x2, y2 = map(int,input("Ingrese las coordenadas del segundo punto x y: ").split())
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

            elif int(y1) == n-1:
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

            elif int(y1) == n-1:
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

            elif int(x1) == n-1:
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
        else:
            print()
            print(Fore.RED+"ERROR: Esas coordenadas no son validas, vuelve a intentarlo"+Fore.RESET)
            print()
            error_coordenadas = True

        if puntos_J1 + puntos_J2 == (n-1)**2:
            partida_finalizada = True

        if error_coordenadas == False:
            print()
            print(Fore.YELLOW+"--------MARCADOR--------"+Fore.RESET)
            print()
            print(f"JUGADOR 1: {puntos_J1} puntos.")
            print(f"JUGADOR 2: {puntos_J2} puntos.")
            print()
            print(Fore.YELLOW+"--------MARCADOR--------"+Fore.RESET)
            print()

if puntos_J1 > puntos_J2 :
    for letra in Fore.GREEN + f"¡EL JUGADOR 1 ({Inicial_J1}) HA GANADO LA PARTIDA!"+ Fore.RESET:
        print(letra, end="", flush=True)
        time.sleep(0.05)
elif puntos_J2 > puntos_J1 :
    for letra in Fore.GREEN+f"¡EL JUGADOR 2 ({Inicial_J2}) HA GANADO LA PARTIDA!"+Fore.RESET:
        print(letra, end="", flush=True)
        time.sleep(0.05)
else:
    for letra in Fore.GREEN+"LA PARTIDA HA ACABADO EN EMPATE"+Fore.RESET:
        print(letra, end="", flush=True)
        time.sleep(0.05)