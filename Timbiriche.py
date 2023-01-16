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
#Después, se pide al usuario que introduzca cuatro valores (x1, y1, x2 e y2) 
#que representan las coordenadas de dos puntos en el tablero
x1 = int(input("Introduce x1 de la primera coordenada: "))
y1 = int(input("Introduce y1 de la primera coordenada: "))
x2 = int(input("Introduce x2 de la segunda coordenada: "))
y2 = int(input("Introduce y2 de la segunda coordenada: "))
#Bucle que se ejecuta mientras el usuario no introduzca "salir" para cualquiera de las coordenadas
while x1 != "salir" and y1!= "salir" and x2 !="salir" and y2 != "salir":
    # Si y1 es igual a y2, cambiar una sección de " " a "-" en el tablero
    if y1==y2:
        #Luego, se vuelve a imprimir la matriz 
        casillero[y1*2][x1*4+1:4*x2]=["-","-","-"]
        for x in range (len(casillero)):
            for j in range (len(casillero[x])):
                print(casillero[x][j],end="")
            print()
     #se vuelven a pedir las coordenadas al usuario. 
    x1 = int(input("Introduce x1 de la primera coordenada: "))
    y1 = int(input("Introduce y1 de la primera coordenada: "))
    x2 = int(input("Introduce x2 de la segunda coordenada: "))
    y2 = int(input("Introduce y2 de la segunda coordenada: "))