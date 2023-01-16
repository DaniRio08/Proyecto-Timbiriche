casillero = [["+"," "," "," ","+"," "," "," ","+"," "," "," ","+"," "," "," ","+"],
             [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
             ["+"," "," "," ","+"," "," "," ","+"," "," "," ","+"," "," "," ","+"],
             [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
             ["+"," "," "," ","+"," "," "," ","+"," "," "," ","+"," "," "," ","+"],
             [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
             ["+"," "," "," ","+"," "," "," ","+"," "," "," ","+"," "," "," ","+"]]

for x in range (len(casillero)):
    for j in range (len(casillero[x])):
        print(casillero[x][j],end="")
    print()
x1 = int(input("Introduce x1 de la primera coordenada: "))
y1 = int(input("Introduce y1 de la primera coordenada: "))
x2 = int(input("Introduce x2 de la segunda coordenada: "))
y2 = int(input("Introduce y2 de la segunda coordenada: "))
while x1 != "salir" and y1!= "salir" and x2 !="salir" and y2 != "salir":
    if y1==y2:
        casillero[y1*2][x1*4+1:4*x2]=["-","-","-"]
        for x in range (len(casillero)):
            for j in range (len(casillero[x])):
                print(casillero[x][j],end="")
            print()
    x1 = int(input("Introduce x1 de la primera coordenada: "))
    y1 = int(input("Introduce y1 de la primera coordenada: "))
    x2 = int(input("Introduce x2 de la segunda coordenada: "))
    y2 = int(input("Introduce y2 de la segunda coordenada: "))