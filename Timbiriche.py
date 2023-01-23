from colorama import init, Fore
init()
import random
import time
print()
#este código utiliza un bucle "for" para imprimir cada letra de una cadena de texto con un efecto de escritura lenta, 
#y utiliza el módulo "Fore" para darle un color específico al texto, 
#y el método sleep del módulo time para detener el programa durante un tiempo específico antes de imprimir la siguiente letra.
frase_bienvenida = Fore.LIGHTBLUE_EX+"BIENVENIDOS AL JUEGO DEL TIMBIRICHE TAMBIÉN CONOCIDO COMO EL JUEGO DE LOS CUADRADOS, SUERTE!!"+Fore.RESET
for letra in frase_bienvenida:
    print(letra, end="", flush=True)
    time.sleep(0.05)
print()
print()
# Variable para indicar si se quiere jugar contra el ordenador o contra otro jugador
versus = input("¿Quieres jugar contra el ordenador(IA) o contra otro jugador(J2)? ")
while (versus != "IA") and (versus != "J2"):
    print("Asegúrate de escribir bien 'IA' o 'J2' dependiendo de contra quien quieras jugar.")
    versus = input("¿Contra quién quieres jugar? ")

# Esta porción de código pide a los jugadores una inicial para identificarse. Luego de forma aleatoria se establece
# quién jugará el primer turno
Inicial_IA = "X"
print()
#Pidiendo la inicial del jugador 1 y validando la longitud de la letra introducida
Inicial_J1 = input("JUGADOR 1, ¿con que letra te quieres identificar? ")
while len(Inicial_J1) != 1 or Inicial_J1 == " ":
    if len(Inicial_J1) > 1:
        print()
        print("Es demasiado largo, solo puede ser una letra :D")
        print()
        Inicial_J1 = input("Vuelve a introducir la letra con la que te quieres identificar: ")
    elif len(Inicial_J1) < 1:
        print()
        print("No has escrito nada :D")
        print()
        Inicial_J1 = input("Vuelve a introducir la letra con la que te quieres identificar: ")
    elif Inicial_J1 == " ":
        print()
        print("No has puesto una inicial :D")
        print()
        Inicial_J1 = input("Vuelve a introducir la letra con la que te quieres identificar: ")
print()
#Si el juego es contra otro jugador, pide la inicial del jugador 2 y valida que no sea la misma que la del jugador 1
if versus == "J2":
    Inicial_J2 = input("JUGADOR 2, ¿con que letra te quieres identificar? ")
    while len(Inicial_J2) != 1 or Inicial_J1==Inicial_J2 or Inicial_J2 == " ":
        if len(Inicial_J2) > 1:
            print()
            print("Es demasiado largo, solo puede ser una letra :D")
            print()
            Inicial_J2 = input("Vuelve a introducir la letra con la que te quieres identificar: ")
        elif len(Inicial_J2) < 1:
            print()
            print("No has escrito nada :D")
            print()
            Inicial_J2 = input("Vuelve a introducir la letra con la que te quieres identificar: ")
        elif Inicial_J2 == " ":
            print()
            print("No has puesto una inicial :D")
            print()
            Inicial_J2 = input("Vuelve a introducir la letra con la que te quieres identificar: ")
        else:
            print()
            print("Has puesto la misma inicial que el JUGADOR 1")
            print()
            Inicial_J2 = input("Vuelve a introducir la letra con la que te quieres identificar: ")

    turno = random.choice([Inicial_J1,Inicial_J2])
    print()
#Si el juego es contra una IA, se selecciona de forma aleatoria quien empieza (jugador o IA)
elif versus == "IA":
    turno = random.choice([Inicial_J1,"IA"])

# Bucle + 'try'/'except' para evitar errores al introducir el tamaño del casillero
while True:
    try:
        n=int(input("Introduce el número de tamaño del casillero (2-10): "))
        break
    except ValueError:
        print()
        print(Fore.RED+"ERROR: No has introducido un número. Inténtalo otra vez :D"+Fore.RESET)
        print()

while n<2 or n>10:
    print()
    print("El tamaño del casillero debe eser como mínimo mayor que 1 y menor 11.")
    print()
    n=int(input("Introduce el número de tamaño del casillero: "))

print()
# Elección random de quién empieza la partida
if versus == "J2":
    if turno == Inicial_J1:
        print(f"Empieza jugando el JUGADOR 1 ({Inicial_J1})")
    elif turno == Inicial_J2:
        print(f"Empieza jugando el JUGADOR 2 ({Inicial_J2})")
elif versus == "IA":
    if turno == Inicial_J1:
        print(f"Empieza jugando el JUGADOR 1 ({Inicial_J1})")
    elif turno == "IA":
        print(f"Empieza jugando el ORDENADOR")
print()
print("-------------------------------------------------------")
print()

# Variables para contar los puntos de cada jugador
puntos_J1 = 0
puntos_J2 = 0
puntos_IA = 0
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

# Creación de listas donde la "IA" va a guarar las coordenadas de los movimientos. Por ejemplo, si antes de poner en esa posición
# el cuadrado tiene 3 líneas el movimiento se guardará en la "lista_3"
lista_0y1 = []
lista_2 = []
lista_3 = []

# Función que verifica cuantas líneas tiene un cuadrado ya dibujadas antes de hacer el movimiento. Devuelve 1, 2 o 3
def verificar_cuantas_líneas(x,y,casillero):
    if ((casillero[y-1][x] == " " and casillero[y+1][x] == " " and casillero[y][x-2] == " " and casillero[y][x+2] == " ")
    or (casillero[y-1][x] != " " and casillero[y+1][x] == " " and casillero[y][x-2] == " " and casillero[y][x+2] == " ")
    or (casillero[y-1][x] == " " and casillero[y+1][x] != " " and casillero[y][x-2] == " " and casillero[y][x+2] == " ")
    or (casillero[y-1][x] == " " and casillero[y+1][x] == " " and casillero[y][x-2] != " " and casillero[y][x+2] == " ")
    or (casillero[y-1][x] == " " and casillero[y+1][x] == " " and casillero[y][x-2] == " " and casillero[y][x+2] != " ")):
        return 1

    elif ((casillero[y-1][x] != " " and casillero[y+1][x] != " " and casillero[y][x-2] == " " and casillero[y][x+2] == " ")
    or (casillero[y-1][x] == " " and casillero[y+1][x] == " " and casillero[y][x-2] != " " and casillero[y][x+2] != " ")
    or (casillero[y-1][x] != " " and casillero[y+1][x] == " " and casillero[y][x-2] != " " and casillero[y][x+2] == " ")
    or (casillero[y-1][x] == " " and casillero[y+1][x] != " " and casillero[y][x-2] != " " and casillero[y][x+2] == " ")
    or (casillero[y-1][x] == " " and casillero[y+1][x] != " " and casillero[y][x-2] == " " and casillero[y][x+2] != " ")
    or (casillero[y-1][x] != " " and casillero[y+1][x] == " " and casillero[y][x-2] == " " and casillero[y][x+2] != " ")):
        return 2
    elif ((casillero[y-1][x] != " " and casillero[y+1][x] != " " and casillero[y][x-2] != " " and casillero[y][x+2] == " ")
    or (casillero[y-1][x] == " " and casillero[y+1][x] != " " and casillero[y][x-2] != " " and casillero[y][x+2] != " ")
    or (casillero[y-1][x] != " " and casillero[y+1][x] != " " and casillero[y][x-2] == " " and casillero[y][x+2] != " ")
    or (casillero[y-1][x] != " " and casillero[y+1][x] == " " and casillero[y][x-2] != " " and casillero[y][x+2] != " ")):
        return 3

# Se define una lista vacia donde van a ir todos los movimientos posibles dependiendo del tamaño del casillero
lista_movimientos = []

# Con un bucle se van añadiendo todos los posibles movimientos a la lista de antes
for y in range(n):
    for x in range(n-1):
        movimiento_v = f"{y} {x},{y} {x+1}"
        lista_movimientos.append(movimiento_v)
        movimiento_h = f"{x} {y},{x+1} {y}"
        lista_movimientos.append(movimiento_h)


# Función para imprimir un casillero, utiliza un ciclo "for" anidado para imprimir cada elemento de la lista en una nueva línea.
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

        # Bucle + 'try'/'except' para evitar errores que cierran el programa al introducir mal una coordenada
        while True:
            try:
                x1, y1 = map(int, input("Introduce las coordenadas del primer punto x y: ").split())
                if x1 not in range(0,n) or y1 not in range(0,n):
                    print(Fore.RED+"ERROR: Has introducido una coordenada fuera del rango permitido. Inténtalo otra vez :D "+Fore.RESET)
                else:
                    break
            except ValueError:
                print(Fore.RED+"ERROR: Has introducido mal la coordenada. Inténtalo otra vez :D"+Fore.RESET)
        while True:
            try:
                x2, y2 = map(int, input("Introduce las coordenadas del segundo punto x y: ").split())
                if x2 not in range(0,n) or y2 not in range(0,n):
                    print(Fore.RED+"ERROR: Has introducido una coordenada fuera del rango permitido. Inténtalo otra vez :D "+Fore.RESET)
                else:
                    break
            except ValueError:
                print(Fore.RED+"ERROR: Has introducido mal la coordenada. Inténtalo otra vez :D"+Fore.RESET)
        print()

         # Bucle para evitar que sea posible introducir la misma línea dos veces
        while (((y1==y2 and x1 + 1 == x2) and (casillero[y1*2][x1*4+1:4*x2] != [" "," "," "]))
        or ((y1==y2 and x1 - 1 == x2) and (casillero[y1*2][x2*4+1:4*x1] != [" "," "," "]))
        or (((x1==x2 and y1 + 1 == y2) or (x1==x2 and y1 - 1 == y2)) and (casillero[y1+y2][x1*4] != " "))):
            print()
            print(Fore.RED+"ERROR: Esa línea ya ha sido dibujada, vuelve a intentarlo"+Fore.RESET)
            print()
            while True:
                try:
                    x1, y1 = map(int, input("Introduce las coordenadas del primer punto x y: ").split())
                    if x1 not in range(0,n) or y1 not in range(0,n):
                        print(Fore.RED+"ERROR: Has introducido una coordenada fuera del rango permitido. Inténtalo otra vez :D "+Fore.RESET)
                    else:
                        break
                except ValueError:
                    print(Fore.RED+"ERROR: Has introducido mal la coordenada. Inténtalo otra vez :D"+Fore.RESET)
            while True:
                try:
                    x2, y2 = map(int, input("Introduce las coordenadas del segundo punto x y: ").split())
                    if x2 not in range(0,n) or y2 not in range(0,n):
                        print(Fore.RED+"ERROR: Has introducido una coordenada fuera del rango permitido. Inténtalo otra vez :D "+Fore.RESET)
                    else:
                        break
                except ValueError:
                    print(Fore.RED+"ERROR: Has introducido mal la coordenada. Inténtalo otra vez :D"+Fore.RESET)
            print()

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
                    casillero[yb][xb]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    if versus == "J2":
                        imprimir_casillero(casillero)
                        turno = Inicial_J2
                    elif versus == "IA":
                        imprimir_casillero(casillero)
                        turno = "IA"

            elif y1 == n-1:
                if verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    if versus == "J2":
                        imprimir_casillero(casillero)
                        turno = Inicial_J2
                    elif versus == "IA":
                        imprimir_casillero(casillero)
                        turno = "IA"

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
                    if versus == "J2":
                        imprimir_casillero(casillero)
                        turno = Inicial_J2
                    elif versus == "IA":
                        imprimir_casillero(casillero)
                        turno = "IA"

            # Eliminación del movimiento realizado de la "lista_movimientos" para que la IA no lo tenga en cuenta
            if versus == "IA":
                lista_movimientos.remove(f"{x1} {y1},{x2} {y2}")

        # Línea horizontal de derecha a izquierda
        elif y1 == y2 and x1 - 1 == x2:
            casillero[y1*2][x2*4+1:4*x1]=[Fore.BLUE+"-","-","-"+Fore.RESET]
            print()

            xb = x2*4+2
            yb = y1*2+1
            xa = x2*4+2
            ya = y1*2-1

            if y1 == 0:
                if verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    casillero[yb][xb]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    if versus == "J2":
                        imprimir_casillero(casillero)
                        turno = Inicial_J2
                    elif versus == "IA":
                        imprimir_casillero(casillero)
                        turno = "IA"

            elif y1 == n-1:
                if verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    casillero[ya][xa]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    if versus == "J2":
                        imprimir_casillero(casillero)
                        turno = Inicial_J2
                    elif versus == "IA":
                        imprimir_casillero(casillero)
                        turno = "IA"

            else :
                 # Verificamos si se cierran ambos cuadrados arriba y abajo
                if (verificar_cuadrado_bajo(xb, yb, casillero) == True) and (verificar_cuadrado_arriba(xa, ya, casillero) == True):
                    # Asignamos el caracter de J1 a ambos cuadrados cerrado
                    casillero[yb][xb]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    casillero[ya][xa]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    # Imprimimos el casillero
                    imprimir_casillero(casillero)
                    # Mostramos un mensaje de dos puntos conseguidos por J!
                    print()
                    print("¡Enhorabuena, has conseguido dos puntos!")
                     # Sumamos dos puntos a J1
                    puntos_J1+=2
                    #Asignamos el turno a J!
                    turno = Inicial_J1
                # Verificamos si se cierra solo el cuadrado arriba
                elif verificar_cuadrado_arriba(xa, ya, casillero) == True:
                    # Asignamos el caracter de J1 al cuadrado cerrado
                    casillero[ya][xa]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    # Imprimimos el casillero
                    imprimir_casillero(casillero)
                    print()
                    # Mostramos un mensaje de punto conseguido por J1
                    print("¡Enhorabuena, has conseguido un punto!")
                    # Sumamos un punto a J1
                    puntos_J1+=1
                    # Asignamos el turno a J1
                    turno = Inicial_J1
                # Verificamos si se cierra solo el cuadrado abajo
                elif verificar_cuadrado_bajo(xb, yb, casillero) == True:
                    # Asignamos el caracter de la IA al cuadrado cerrado
                    casillero[yb][xb]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    # Imprimimos el casillero
                    imprimir_casillero(casillero)
                    print()
                     # Mostramos un mensaje de punto conseguido por J!
                    print("¡Enhorabuena, has conseguido un punto!")

                    # Sumamos un punto a J1
                    puntos_J1+=1
                    # Asignamos el turno a J1
                    turno = Inicial_J1
                else:
                    if versus == "J2":
                        imprimir_casillero(casillero)
                        turno = Inicial_J2
                    elif versus == "IA":
                        imprimir_casillero(casillero)
                        turno = "IA"
            
            # Eliminación del movimiento realizado de la "lista_movimientos" para que la IA no lo tenga en cuenta
            if versus == "IA":
                lista_movimientos.remove(f"{x2} {y2},{x1} {y1}")
        
       
        elif (x1==x2 and y1 + 1 == y2) or (x1==x2 and y1 - 1 == y2):
            casillero[y1 + y2][x1*4]= Fore.BLUE+"|"+Fore.RESET
            print()

            xi = x1*4-2
            yi = y1 + y2
            xd = x1*4+2
            yd = y1 + y2

            if x1 == 0:
                if verificar_cuadrado_dcha(xd,yd,casillero) == True:
                    casillero[yd][xd]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    if versus == "J2":
                        imprimir_casillero(casillero)
                        turno = Inicial_J2
                    elif versus == "IA":
                        imprimir_casillero(casillero)
                        turno = "IA"

            elif x1 == n-1:
                if verificar_cuadrado_izda(xi,yi,casillero) == True:
                    casillero[yi][xi]=Fore.BLUE+f"{Inicial_J1}"+Fore.RESET
                    imprimir_casillero(casillero)
                    print()
                    print("¡Enhorabuena, has conseguido un punto!")
                    puntos_J1+=1
                    turno = Inicial_J1
                else:
                    if versus == "J2":
                        imprimir_casillero(casillero)
                        turno = Inicial_J2
                    elif versus == "IA":
                        imprimir_casillero(casillero)
                        turno = "IA"

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
                    if versus == "J2":
                        imprimir_casillero(casillero)
                        turno = Inicial_J2
                    elif versus == "IA":
                        imprimir_casillero(casillero)
                        turno = "IA"
            
            # Eliminación del movimiento realizado de la "lista_movimientos" para que la IA no lo tenga en cuenta
            if versus == "IA":
                if y1 < y2:
                    lista_movimientos.remove(f"{x1} {y1},{x2} {y2}")
                if y1 > y2:
                    lista_movimientos.remove(f"{x2} {y2},{x1} {y1}")

        # Condición para que si se introduce una coordenada no válida el programa no se quede pillado pidiendo coordenadas
        else:
            print(Fore.RED+"ERROR: Esas coordenadas no son validas. Inténtalo otra vez :D"+Fore.RESET)
            print()
            error_coordenadas = True

        if versus == "J2":
            if puntos_J1 + puntos_J2 == (n-1)**2:
                partida_finalizada = True
        elif versus == "IA":
            if puntos_J1 + puntos_IA == (n-1)**2:
                partida_finalizada = True
        
        if versus == "J2":
            if error_coordenadas == False:
                print()
                print(Fore.YELLOW+"--------MARCADOR--------"+Fore.RESET)
                print()
                print(f"JUGADOR 1: {puntos_J1} puntos.")
                print(f"JUGADOR 2: {puntos_J2} puntos.")
                print()
                print(Fore.YELLOW+"--------MARCADOR--------"+Fore.RESET)
                print()
        
        elif versus == "IA":
            if error_coordenadas == False:
                print()
                print(Fore.YELLOW+"-------MARCADOR-------"+Fore.RESET)
                print()
                print(f"TÚ: {puntos_J1} puntos.")
                print(f"IA: {puntos_IA} puntos.")
                print()
                print(Fore.YELLOW+"-------MARCADOR-------"+Fore.RESET)
                print()

    elif versus == "J2":
        if turno == Inicial_J2:
            if error_coordenadas == False:
                print()
                print(f"Turno JUGADOR 2 ({Inicial_J2})")
                print()
            error_coordenadas = False
            while True:
                try:
                    x1, y1 = map(int, input("Introduce las coordenadas del primer punto x y: ").split())
                    if x1 not in range(0,n) or y1 not in range(0,n):
                        print(Fore.RED+"ERROR: Has introducido una coordenada fuera del rango permitido. Inténtalo otra vez :D "+Fore.RESET)
                    else:
                        break
                except ValueError:
                    print(Fore.RED+"ERROR: Has introducido mal la coordenada. Inténtalo otra vez :D"+Fore.RESET)
            while True:
                try:
                    x2, y2 = map(int, input("Introduce las coordenadas del segundo punto x y: ").split())
                    if x2 not in range(0,n) or y2 not in range(0,n):
                        print(Fore.RED+"ERROR: Has introducido una coordenada fuera del rango permitido. Inténtalo otra vez :D "+Fore.RESET)
                    else:
                        break
                except ValueError:
                    print(Fore.RED+"ERROR: Has introducido mal la coordenada. Inténtalo otra vez :D"+Fore.RESET)
            print()
            while (((y1==y2 and x1 + 1 == x2) and (casillero[y1*2][x1*4+1:4*x2] != [" "," "," "]))
            or ((y1==y2 and x1 - 1 == x2) and (casillero[y1*2][x2*4+1:4*x1] != [" "," "," "]))
            or (((x1==x2 and y1 + 1 == y2) or (x1==x2 and y1 - 1 == y2)) and (casillero[y1+y2][x1*4] != " "))):
                print()
                print(Fore.RED+"ERROR: Esa línea ya ha sido dibujada, vuelve a intentarlo"+Fore.RESET)
                print()
                while True:
                    try:
                        x1, y1 = map(int, input("Introduce las coordenadas del primer punto x y: ").split())
                        if x1 not in range(0,n) or y1 not in range(0,n):
                            print(Fore.RED+"ERROR: Has introducido una coordenada fuera del rango permitido. Inténtalo otra vez :D "+Fore.RESET)
                        else:
                            break
                    except ValueError:
                        print(Fore.RED+"ERROR: Has introducido mal la coordenada. Inténtalo otra vez :D"+Fore.RESET)
                while True:
                    try:
                        x2, y2 = map(int, input("Introduce las coordenadas del segundo punto x y: ").split())
                        if x2 not in range(0,n) or y2 not in range(0,n):
                            print(Fore.RED+"ERROR: Has introducido una coordenada fuera del rango permitido. Inténtalo otra vez :D "+Fore.RESET)
                        else:
                            break
                    except ValueError:
                        print(Fore.RED+"ERROR: Has introducido mal la coordenada. Inténtalo otra vez :D"+Fore.RESET)
            # Línea horizontal de izquierda a derecha
            if y1==y2 and x1 + 1 == x2:
                casillero[y1*2][x1*4+1:4*x2]=[Fore.RED+"-","-","-"+Fore.RESET]
                print()

                xb = x1*4+2
                yb = y1*2+1
                xa = x1*4+2
                ya = y1*2-1
                
                if y1 == 0:
                    # Verificamos si se cierra el cuadrado abajo
                    if verificar_cuadrado_bajo(xb, yb, casillero) == True:
                         # Asignamos el caracter de la IA al cuadrado cerrado
                        casillero[yb][xb]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                        # Imprimimos el casillero
                        imprimir_casillero(casillero)
                         # Mostramos un mensaje de punto conseguido por J2
                        print()
                        print("¡Enhorabuena, has conseguido un punto!")
                        # Sumamos un punto a J2
                        puntos_J2+=1
                         # Asignamos el turno a J2
                        turno = Inicial_J2
                    else:
                        # Si no se cierra el cuadrado, se le asigna el turno al jugador
                        imprimir_casillero(casillero)
                        print()
                        turno = Inicial_J1

                elif y1 == n-1:
                     # Verificamos si se cierra el cuadrado arriba
                    if verificar_cuadrado_arriba(xa, ya, casillero) == True:
                         #Asignamos el caracter de la IA al cuadrado cerrado
                        casillero[ya][xa]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                          # Imprimimos el casillero
                        imprimir_casillero(casillero)
                        # Mostramos un mensaje de punto conseguido por J2
                        print()
                        print("¡Enhorabuena, has conseguido un punto!")
                        # Sumamos un punto a J2
                        puntos_J2+=1
                         # Asignamos el turno a J2
                        turno = Inicial_J2
                    else:
                        # Si no se cierra el cuadrado, se le asigna el turno al jugador
                        imprimir_casillero(casillero)
                        print()
                        turno = Inicial_J1

                else :
                     # Verificamos si se cierran ambos cuadrados arriba y abajo
                    if (verificar_cuadrado_bajo(xb, yb, casillero) == True) and (verificar_cuadrado_arriba(xa, ya, casillero) == True):
                        # Asignamos el caracter de la J2 a ambos cuadrados cerrado
                        casillero[yb][xb]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                        casillero[ya][xa]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                        # Imprimimos el casillero
                        imprimir_casillero(casillero)
                        print()
                         # Mostramos un mensaje de dos puntos conseguidos por J2
                        print("¡Enhorabuena, has conseguido dos puntos!")
                        # Sumamos dos puntos a J2
                        puntos_J2+=2
                         # Asignamos el turno a J2
                        turno = Inicial_J2
                    # Verificamos si se cierra solo el cuadrado arriba
                    elif verificar_cuadrado_arriba(xa, ya, casillero) == True:
                         # Asignamos el caracter de J2 al cuadrado cerrado
                        casillero[ya][xa]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                        # Imprimimos el casillero
                        imprimir_casillero(casillero)
                        print()
                        # Mostramos un mensaje de punto conseguido por J2
                        print("¡Enhorabuena, has conseguido un punto!")
                        # Sumamos un punto a J2
                        puntos_J2+=1
                        # Asignamos el turno a J2
                        turno = Inicial_J2
                     # Verificamos si se cierra solo el cuadrado abajo
                    elif verificar_cuadrado_bajo(xb, yb, casillero) == True:
                         # Asignamos el caracter de J2 al cuadrado cerrado
                        casillero[yb][xb]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                        # Imprimimos el casillero
                        imprimir_casillero(casillero)
                         # Mostramos un mensaje de punto conseguido por J2
                        print()
                        print("¡Enhorabuena, has conseguido un punto!")
                        # Sumamos un punto a J2
                        puntos_J2+=1
                        # Asignamos el turno a J2
                        turno = Inicial_J2
                    else:
                         # Si no se cierra ninguno de los cuadrados, se le asigna el turno al jugadorJ1
                        imprimir_casillero(casillero)
                        print()
                        turno = Inicial_J1

            # Línea horizontal de derecha a izquierda
            elif y1==y2 and x1 - 1 == x2:
                casillero[y1*2][x2*4+1:4*x1]=[Fore.RED+"-","-","-"+Fore.RESET]
                print()

                xb = x2*4+2
                yb = y1*2+1
                xa = x2*4+2
                ya = y1*2-1

                if y1 == 0:
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

                elif y1 == n-1:
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
            elif (x1==x2 and y1 + 1 == y2) or (x1==x2 and y1 - 1 == y2):
                casillero[y1+y2][x1*4]= Fore.RED+"|"+Fore.RESET
                print()

                xi = x1*4-2
                yi = y1 + y2
                xd = x1*4+2
                yd = y1 + y2

                if x1 == 0:
                     # Verificamos si se cierra solo el cuadrado a la derecha
                    if verificar_cuadrado_dcha(xd,yd,casillero) == True:
                        # Asignamos el caracter del jugador al cuadrado cerrado
                        casillero[yd][xd]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                        # Imprimimos el casillero
                        imprimir_casillero(casillero)
                        print()
                        # Mostramos un mensaje de punto conseguido
                        print("¡Enhorabuena, has conseguido un punto!")
                        # Sumamos un punto al jugador
                        puntos_J2+=1
                        # Asignamos el turno al jugador
                        turno = Inicial_J2
                    else:
                         #Si no  se imprime el casillero y cambiamos de turno
                        imprimir_casillero(casillero)
                        print()
                        turno = Inicial_J1

                elif x1 == n-1:
                    # Verificamos si se cierra solo el cuadrado a izquierda
                    if verificar_cuadrado_izda(xi,yi,casillero) == True:
                        # Asignamos el caracter del jugador al cuadrado cerrado
                        casillero[yi][xi]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                        # Imprimimos el casillero
                        imprimir_casillero(casillero)
                        print()
                        # Mostramos un mensaje de punto conseguido
                        print("¡Enhorabuena, has conseguido un punto!")
                        # Sumamos un punto al jugador
                        puntos_J2+=1
                        # Asignamos el turno al jugador
                        turno = Inicial_J2
                    else:
                        #Si no  se imprime el casillero y cambiamos de turno
                        imprimir_casillero(casillero)
                        print()
                        turno = Inicial_J1

                else:
                    # Verificamos si se cierran ambos cuadrados a la izquierda y derecha
                    if (verificar_cuadrado_dcha(xd,yd,casillero) == True) and (verificar_cuadrado_izda(xi,yi,casillero) == True):
                        # Asignamos el caracter del jugador a ambos cuadrados cerrados
                        casillero[yd][xd]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                        casillero[yi][xi]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                        # Imprimimos el casillero
                        imprimir_casillero(casillero)
                        print()
                         # Mostramos un mensaje de dos puntos conseguidos
                        print("¡Enhorabuena, has conseguido dos puntos!")
                        # Sumamos dos puntos al jugador
                        puntos_J2+=2
                        # Asignamos el turno al jugador2
                        turno = Inicial_J2     
                    # Verificamos si se cierra solo el cuadrado a la derecha
                    elif verificar_cuadrado_dcha(xd,yd,casillero) == True:
                         # Asignamos el caracter del jugador al cuadrado cerrado
                        casillero[yd][xd]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                        # Imprimimos el casillero
                        imprimir_casillero(casillero)
                        print()
                        # Mostramos un mensaje de punto conseguido
                        print("¡Enhorabuena, has conseguido un punto!")
                         # Sumamos un punto al jugador2
                        puntos_J2+=1
                          # Asignamos el turno al jugador2
                        turno = Inicial_J2
                    # Verificamos si se cierra solo el cuadrado a la izquierda
                    elif verificar_cuadrado_izda(xi,yi,casillero) == True:
                        # Asignamos el caracter del jugador al cuadrado cerrado
                        casillero[yi][xi]=Fore.RED+f"{Inicial_J2}"+Fore.RESET
                        #Imprimimos el casillero
                        imprimir_casillero(casillero)
                        print()
                         # Mostramos un mensaje de punto conseguido
                        print("¡Enhorabuena, has conseguido un punto!")
                         # Sumamos un punto al jugador
                        puntos_J2+=1
                        # Asignamos el turno al jugador
                        turno = Inicial_J2
                    else:
                        #Si no  se imprime el casillero y cambiamos de turno
                        imprimir_casillero(casillero)
                        print()
                        turno = Inicial_J1
            else:
                
                print(Fore.RED+"ERROR: Esas coordenadas no son validas. Inténtalo otra vez :D"+Fore.RESET)
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

    elif versus == "IA":
        if turno == "IA":
            # La "IA" recprre la lista que contiene todos los movimientos posibles
            for coordenadas in lista_movimientos:
                # Se transforma la coordenada que está toda escrita como un string a las variables x1, y1, x2, y2
                x1 = int(coordenadas[0])
                y1 = int(coordenadas[2])
                x2 = int(coordenadas[4])
                y2 = int(coordenadas[6])
                # Condición para las líneas horizontales
                if y1==y2 and x1 + 1 == x2:
                    # Igual que con la función "verificar cuadrados" una línea horizontal solo puede cerrar el cuadrado de arriba 
                    # y el de abajo. Por lo que transformamos las coordenadas en el punto central del cuadrado de arriba y el de abajo
                    xb = x1*4+2
                    yb = y1*2+1
                    xa = x1*4+2
                    ya = y1*2-1
                    # En el caso de que la línea sea la de arriba solo puede formar un cuadrado abajo
                    if y1 == 0:
                        # Llamando a la función "verificar_cuantas_líneas" con las coordenadas del punto central del cuadrado de abajo
                        # y dependiendo de si devuelve 1, 2 o 3 se añade la coordenada en una lista u otra
                        if verificar_cuantas_líneas(xb,yb,casillero) == 1:
                            lista_0y1.append(coordenadas)
                        elif verificar_cuantas_líneas(xb,yb,casillero) == 2:
                            lista_2.append(coordenadas)
                        elif verificar_cuantas_líneas(xb,yb,casillero) == 3:
                            lista_3.append(coordenadas)
                    # En el caso de que la línea sea la de abajo solo puede formar el cuadrado de arriba
                    elif y1 == n-1:
                        # Lo mismo que antes pero introduciendo las coordenadas del cuadrado de arriba
                        if verificar_cuantas_líneas(xa,ya,casillero) == 1:
                            lista_0y1.append(coordenadas)
                        elif verificar_cuantas_líneas(xa,ya,casillero) == 2:
                            lista_2.append(coordenadas)
                        elif verificar_cuantas_líneas(xa,ya,casillero) == 3:
                            lista_3.append(coordenadas)
                    else:
                        # Si la línea puede cerrar 2 cuadrados solo nos interesa almacenar la coordenadas una vez y en la lista
                        # que corresponda al mayor número de líneas posibles
                        if (verificar_cuantas_líneas(xa,ya,casillero)) == 1 and (verificar_cuantas_líneas(xb,yb,casillero) == 1):
                            lista_0y1.append(coordenadas)
                        elif ((verificar_cuantas_líneas(xa,ya,casillero)) == 2 and (verificar_cuantas_líneas(xb,yb,casillero) == 2)
                        or (verificar_cuantas_líneas(xa,ya,casillero)) == 1 and (verificar_cuantas_líneas(xb,yb,casillero) == 2)
                        or (verificar_cuantas_líneas(xa,ya,casillero)) == 2 and (verificar_cuantas_líneas(xb,yb,casillero) == 1)):
                            lista_2.append(coordenadas)
                        else:
                            lista_3.append(coordenadas)

                # Lo mismo pero para las líneas verticales. Lo único que cambia es que una línea vertical solo puede cerrar el cuadrado
                # de la derecha y el de la izquierda, en vez del de arriba y el de abajo
                elif x1==x2 and y1 + 1 == y2:
                    xi = x1*4-2
                    yi = y1 + y2
                    xd = x1*4+2
                    yd = y1 + y2
                    if x1 == 0:
                        if verificar_cuantas_líneas(xd,yd,casillero) == 1:
                            lista_0y1.append(coordenadas)
                        elif verificar_cuantas_líneas(xd,yd,casillero) == 2:
                            lista_2.append(coordenadas)
                        elif verificar_cuantas_líneas(xd,yd,casillero) == 3:
                            lista_3.append(coordenadas)
                    elif x1 == n-1:
                        if verificar_cuantas_líneas(xi,yi,casillero) == 1:
                            lista_0y1.append(coordenadas)
                        elif verificar_cuantas_líneas(xi,yi,casillero) == 2:
                            lista_2.append(coordenadas)
                        elif verificar_cuantas_líneas(xi,yi,casillero) == 3:
                            lista_3.append(coordenadas)
                    else:
                        if (verificar_cuantas_líneas(xd,yd,casillero)) == 1 and (verificar_cuantas_líneas(xi,yi,casillero) == 1):
                            lista_0y1.append(coordenadas)
                        elif ((verificar_cuantas_líneas(xd,yd,casillero)) == 2 and (verificar_cuantas_líneas(xi,yi,casillero) == 2)
                        or (verificar_cuantas_líneas(xd,yd,casillero)) == 1 and (verificar_cuantas_líneas(xi,yi,casillero) == 2)
                        or (verificar_cuantas_líneas(xd,yd,casillero)) == 2 and (verificar_cuantas_líneas(xi,yi,casillero) == 1)):
                            lista_2.append(coordenadas)
                        else:
                            lista_3.append(coordenadas)

            # Todos los cuadrados que tengan 3 líneas dibujadas antes de hacer el movimiento significan que si se pone se cierra un 
            # cuadrado, por lo que si la lista no está vacía se debe priorizar poner uno de ella.
            if len(lista_3) != 0:
                jugada = random.choice(lista_3)
            # Lo segundo mejor es poner una línea donde solo haya o bien 0 o 1 línea dibujada anteriormente. Será lo segundo en priorizarse
            elif len(lista_0y1) != 0:
                jugada = random.choice(lista_0y1)
            # En el caso de que las otras listas estén vacías significará que la única opción es poner una línea en un cuadrado
            # que ya tiene 2, lo que significa que en el rival en el siguiente turno cerrará al menos un cuadrado. Por eso es la última 
            # opción
            else :
                jugada = random.choice(lista_2)
            time.sleep(0.85)
            # Transformar la jugada en coordenadas validas y hacer un turno exactamente igual que Jugador1 o Jugador2
            x1 = int(jugada[0])
            y1 = int(jugada[2])
            x2 = int(jugada[4])
            y2 = int(jugada[6])
            print()
            print(f"ORDENADOR: dibujo esta línea: {x1} {y1},{x2} {y2}")
            print()
            # Línea horizontal
            if y1==y2 and x1 + 1 == x2:
                 # Asignamos el color rojo a la línea unida
                casillero[y1*2][x1*4+1:4*x2]=[Fore.RED+"-","-","-"+Fore.RESET]
                print()
              # Calculamos las posiciones de los cuadrados arriba y abajo de la línea unida
                xb, yb, xa, ya = x1*4+2, y1*2+1, x1*4+2, y1*2-1
                if y1 == 0:
                    if verificar_cuadrado_bajo(xb, yb, casillero) == True:
                        # Asignamos el caracter de la IA al cuadrado cerrado
                        casillero[yb][xb]=Fore.RED+f"{Inicial_IA}"+Fore.RESET
                        # Imprimimos el casillero
                        imprimir_casillero(casillero)
                        # Mostramos un mensaje de punto conseguido por la IA
                        print()
                        print("ORDENADOR: ¡He conseguido un punto!")
                        # Sumamos un punto a la IA
                        puntos_IA+=1
                        # Asignamos el turno a la IA
                        turno = "IA"
                    else:
                         # Si no se cierra el cuadrado, se le asigna el turno al jugador
                        imprimir_casillero(casillero)
                        print()
                        turno = Inicial_J1
                # Verificamos si se cierra el cuadrado arriba

                elif y1 == n-1:
                    if verificar_cuadrado_arriba(xa, ya, casillero) == True:
                        #Asignamos el caracter de la IA al cuadrado cerrado
                        casillero[ya][xa]=Fore.RED+f"{Inicial_IA}"+Fore.RESET
                         # Imprimimos el casillero
                        imprimir_casillero(casillero)
                        # Mostramos un mensaje de punto conseguido por la IA
                        print()
                        print("ORDENADOR: ¡He conseguido un punto!")
                        # Sumamos un punto a la IA
                        puntos_IA+=1
                        # Asignamos el turno a la IA
                        turno = "IA"
                    else:
                        # Si no se cierra el cuadrado, se le asigna el turno al jugador
                        imprimir_casillero(casillero)
                        print()
                        turno = Inicial_J1

                else :
                    if (verificar_cuadrado_bajo(xb, yb, casillero) == True) and (verificar_cuadrado_arriba(xa, ya, casillero) == True):
                        # Asignamos el caracter de la IA a ambos cuadrados cerrado
                        casillero[yb][xb]=Fore.RED+f"{Inicial_IA}"+Fore.RESET
                        casillero[ya][xa]=Fore.RED+f"{Inicial_IA}"+Fore.RESET
                        # Imprimimos el casillero
                        imprimir_casillero(casillero)
                        # Mostramos un mensaje de dos puntos conseguidos por la IA
                        print()
                        print("ORDENADOR: ¡He conseguido dos puntos!")
                        # Sumamos dos puntos a la IA
                        puntos_IA+=2
                        # Asignamos el turno a la IA
                        turno = "IA"
                    # Verificamos si se cierra solo el cuadrado arriba
                    elif verificar_cuadrado_arriba(xa, ya, casillero) == True:
                         # Asignamos el caracter de la IA al cuadrado cerrado
                        casillero[ya][xa]=Fore.RED+f"{Inicial_IA}"+Fore.RESET
                        # Imprimimos el casillero
                        imprimir_casillero(casillero)
                        # Mostramos un mensaje de punto conseguido por la IA
                        print()
                        print("ORDENADOR: ¡He conseguido un punto!")
                        # Sumamos un punto a la IA
                        puntos_IA+=1
                        # Asignamos el turno a la IA
                        turno = "IA"
                    # Verificamos si se cierra solo el cuadrado abajo
                    elif verificar_cuadrado_bajo(xb, yb, casillero) == True:
                        # Asignamos el caracter de la IA al cuadrado cerrado
                        casillero[yb][xb]=Fore.RED+f"{Inicial_IA}"+Fore.RESET
                        # Imprimimos el casillero
                        imprimir_casillero(casillero)
                        # Mostramos un mensaje de punto conseguido por la IA
                        print()
                        print("ORDENADOR: ¡He conseguido un punto!")
                        # Sumamos un punto a la IA
                        puntos_IA+=1
                        # Asignamos el turno a la IA
                        turno = "IA"
                    else:
                         # Si no se cierra ninguno de los cuadrados, se le asigna el turno al jugador
                            imprimir_casillero(casillero)
                            print()
                            turno = Inicial_J1

            # Línea vertical
            elif x1==x2 and y1 + 1 == y2:
                casillero[y1+y2][x1*4]= Fore.RED+"|"+Fore.RESET
                xi = x1*4-2
                yi = y1 + y2
                xd = x1*4+2
                yd = y1 + y2

                if x1 == 0:
                    if verificar_cuadrado_dcha(xd,yd,casillero) == True:
                            casillero[yd][xd]=Fore.RED+f"{Inicial_IA}"+Fore.RESET
                            imprimir_casillero(casillero)
                            print()
                            print("ORDENADOR: ¡He conseguido un punto!")
                            puntos_IA+=1
                            turno = "IA"
                    else:
                            imprimir_casillero(casillero)
                            print()
                            turno = Inicial_J1

                elif x1 == n-1:
                    if verificar_cuadrado_izda(xi,yi,casillero) == True:
                            casillero[yi][xi]=Fore.RED+f"{Inicial_IA}"+Fore.RESET
                            imprimir_casillero(casillero)
                            print()
                            print("ORDENADOR: ¡He conseguido un punto!")
                            puntos_IA+=1
                            turno = "IA"
                    else:
                            imprimir_casillero(casillero)
                            print()
                            turno = Inicial_J1

                else:
                    if (verificar_cuadrado_dcha(xd,yd,casillero) == True) and (verificar_cuadrado_izda(xi,yi,casillero) == True):
                            casillero[yd][xd]=Fore.RED+f"{Inicial_IA}"+Fore.RESET
                            casillero[yi][xi]=Fore.RED+f"{Inicial_IA}"+Fore.RESET
                            imprimir_casillero(casillero)
                            print()
                            print("ORDENADOR: ¡He conseguido dos puntoS!")
                            puntos_IA+=2
                            turno = "IA"      
                    elif verificar_cuadrado_dcha(xd,yd,casillero) == True:
                            casillero[yd][xd]=Fore.RED+f"{Inicial_IA}"+Fore.RESET
                            imprimir_casillero(casillero)
                            print()
                            print("ORDENADOR: ¡He conseguido un punto!")
                            puntos_IA+=1
                            turno = "IA"
                    elif verificar_cuadrado_izda(xi,yi,casillero) == True:
                            casillero[yi][xi]=Fore.RED+f"{Inicial_IA}"+Fore.RESET
                            imprimir_casillero(casillero)
                            print()
                            print("ORDENADOR: ¡He conseguido un punto!")
                            puntos_IA+=1
                            turno = "IA"
                    else:
                            imprimir_casillero(casillero)
                            print()
                            turno = Inicial_J1
            
            # Marcador
            print()
            print(Fore.YELLOW+"-------MARCADOR-------"+Fore.RESET)
            print()
            print(f"TÚ: {puntos_J1} puntos.")
            print(f"IA: {puntos_IA} puntos.")
            print()
            print(Fore.YELLOW+"-------MARCADOR-------"+Fore.RESET)
            print()

            # Se vuelven a definir las listas 1, 2 y 3 para que en el siguiente turno solo se almacene la nueva información de la 
            # situación del casillero
            lista_0y1 = []
            lista_2 = []
            lista_3 = []

            # Se elimina la jugada de la lista de movimientos para que no se pueda volver a elegir. Habra que hacer que cuando juegue el 
            # Jugador1 también se elimine su jugada de está lista
            lista_movimientos.remove(jugada)

            # Condición finalizar partida
            if puntos_IA + puntos_J1== (n-1)**2:
                partida_finalizada = True


if versus == "J2":
    if puntos_J1 > puntos_J2 :
         # imprimir mensaje de victoria para Jugador 1
        for letra in Fore.GREEN + f"¡EL JUGADOR 1 ({Inicial_J1}) HA GANADO LA PARTIDA!"+ Fore.RESET:
            print(letra, end="", flush=True)
            time.sleep(0.05)
    elif puntos_J2 > puntos_J1 :
         # imprimir mensaje de victoria para Jugador 2
        for letra in Fore.GREEN+f"¡EL JUGADOR 2 ({Inicial_J2}) HA GANADO LA PARTIDA!"+Fore.RESET:
            print(letra, end="", flush=True)
            time.sleep(0.05)
    else:
        # imprimir mensaje de empate
        for letra in Fore.GREEN+"LA PARTIDA HA ACABADO EN EMPATE"+Fore.RESET:
            print(letra, end="", flush=True)
            time.sleep(0.05)

if versus == "IA":
    if puntos_J1 > puntos_IA :
         # imprimir mensaje de victoria para el jugador contra la IA
        for letra in Fore.GREEN + "¡HAS CONSEGUIDO GANARLE AL ORDENADOR, ENHORABUENA!"+ Fore.RESET:
            print(letra, end="", flush=True)
            time.sleep(0.05)

    elif puntos_IA > puntos_J1 :
       # imprimir mensaje de derrota para el jugador contra la IA
        for letra in Fore.RED+f"¡HAS PERDIDO, EL ORDENADOR TE HA GANADO!"+Fore.RESET:
            print(letra, end="", flush=True)
            time.sleep(0.05)
    else:
        # imprimir mensaje de empate
        for letra in Fore.YELLOW+"LA PARTIDA HA ACABADO EN EMPATE"+Fore.RESET:
            print(letra, end="", flush=True)
            time.sleep(0.05)