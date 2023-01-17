from colorama import init, Fore
init()
inicial = "H"
turno = "jugador1"

# Función que verifica si se ha formado un cuadrado al introducir una línea horizontal.
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

# Función que verifica si se ha formado un cuadrado al introducir una línea vertical.
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
for x in range (len(casillero)):
    for j in range (len(casillero[x])):
        print(casillero[x][j],end="")
    print()

if turno == "jugador1":
    # Petición de coordenadas
    x1, y1 = input("Introduce las coordenadas del primer punto x y: ").split()
    x2, y2 = input("Introduce las coordenadas del segundo punto x y: ").split()
    # Bucle que dibuja la línea que quiere el jugador y vuelve a pedir coordenadas
    while x1 != "salir" or y1!= "salir" or x2 !="salir" or y2 != "salir":
        x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
        # Línea horizontal de izquierda a derecha
        if y1==y2 and x1 + 1 == x2:
            casillero[y1*2][x1*4+1:4*x2]=[Fore.BLUE+"-","-","-"+Fore.RESET]
            print()

            # Nuevas coordenadas que representan el punto central del cuadrado de arriba y el de abajo que se usan para verificar 
            # si se ha cerrado un cuadrado
            xb = x1*4+2
            yb = y1*2+1
            xa = x1*4+2
            ya = y1*2-1
            
            # Cada línea puede cerrar dos cuadrados, excepto las que se situan en los bordes del tablero. Si no se hace esta excepción
            # surgen errores que no dejan continuar la partida
            if y1 == 0:
                if verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()
                else:
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

            elif y1 == 4:
                if verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                else:
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

            else :
                # Este condicional evalua si se han cerrado dos cuadrados a la vez. Si no se incluye, al cerrar dos cuadrados
                # simultanemente solo cuenta únicamente como uno cerrado
                if (verificar_cuadrado_bajo(xb, yb, casillero) == True) and (verificar_cuadrado_arriba(xa, ya, casillero) == True):
                    casillero[yb][xb]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    casillero[ya][xa]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                elif verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                elif verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                else:
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

        # Línea horizontal de derecha a izquierda
        elif y1==y2 and x1 - 1 == x2:
            casillero[y1*2][x2*4+1:4*x1]=[Fore.BLUE+"-","-","-"+Fore.RESET]
            print()

            xb = x2*4+2
            yb = y1*2+1
            xa = x2*4+2
            ya = y1*2-1

            if y1 == 0:
                if verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                else:
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

            elif y1 == 4:
                if verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                else:
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

            else :
                if (verificar_cuadrado_bajo(xb, yb, casillero) == True) and (verificar_cuadrado_arriba(xa, ya, casillero) == True):
                    casillero[yb][xb]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    casillero[ya][xa]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                elif verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                elif verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                else:
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()
        
        # Líneas verticales
        elif (x1==x2 and y1 + 1 == y2) or (x1==x2 and y1 - 1 == y2):
            casillero[y1+y2][x1*4]= Fore.BLUE+"|"+Fore.RESET
            print()

            xi = x1*4-2
            yi = y1 + y2
            xd = x1*4+2
            yd = y1 + y2

            if x1 == 0:
                if verificar_cuadrado_dcha(xd,yd,casillero) == True:
                    casillero[yd][xd]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                else:
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()


            elif x1 == 4:
                if verificar_cuadrado_izda(xi,yi,casillero) == True:
                    casillero[yi][xi]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                else:
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

            else: 
                if (verificar_cuadrado_dcha(xd,yd,casillero) == True) and (verificar_cuadrado_izda(xi,yi,casillero) == True):
                    casillero[yd][xd]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    casillero[yi][xi]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                elif verificar_cuadrado_dcha(xd,yd,casillero) == True:
                    casillero[yd][xd]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()

                elif verificar_cuadrado_izda(xi,yi,casillero) == True:
                    casillero[yi][xi]=Fore.BLUE+f"{inicial}"+Fore.RESET
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()
                    
                else:
                    for x in range (len(casillero)):
                        for j in range (len(casillero[x])):
                            print(casillero[x][j],end="")
                        print()
        x1, y1 = input("Introduce las coordenadas del primer punto x y: ").split()
        x2, y2 = input("Introduce las coordenadas del segundo punto x y: ").split()