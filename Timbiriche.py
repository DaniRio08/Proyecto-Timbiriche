from colorama import init, Fore
init()
#Creación de una matriz de casilleros vacíos 
casillero = [["+"," "," "," ","+"," "," "," ","+"," "," "," ","+"," "," "," ","+"],
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
# Petición de coordenadas.
x1, y1 = input("Ingrese las coordenadas del primer punto x y: ").split()
x2, y2 = input("Ingrese las coordenadas del segundo punto x y: ").split()
# Bucle que dibuja la línea que desea el jugador y vuelve a pedir coordenadas.
while x1 != "salir" or y1!= "salir" or x2 !="salir" or y2 != "salir":
    x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
    # Línea horizontal de izquierda a derecha.
    if y1==y2 and x1 + 1 == x2:
        casillero[y1*2][x1*4+1:4*x2]=[Fore.BLUE+"-","-","-"+Fore.RESET]
        for x in range (len(casillero)):
            for j in range (len(casillero[x])):
                print(casillero[x][j],end="")
            print()
    # Línea horizontal de derecha a izquierda.
    elif y1==y2 and x1 - 1 == x2:
        casillero[y1*2][x2*4+1:4*x1]=[Fore.BLUE+"-","-","-"+Fore.RESET]
        for x in range (len(casillero)):
            for j in range (len(casillero[x])):
                print(casillero[x][j],end="")
            print()
    # Líneas verticales.
    elif (x1==x2 and y1 + 1 == y2) or (x1==x2 and y1 - 1 == y2):
        casillero[y1+y2][x1*4]= Fore.BLUE+"|"+Fore.RESET
        for x in range (len(casillero)):
            for j in range (len(casillero[x])):
                print(casillero[x][j],end="")
            print()

    x1, y1 = input("Ingrese las coordenadas del primer punto x y :").split()
    x2, y2 = input("Ingrese las coordenadas del segundo punto x y :").split()