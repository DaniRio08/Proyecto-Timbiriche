# Proyecto Juego Timbiriche
##### Por Dani Río y Raúl Velásquez
---
### Objetivos
El objetivo de este proyecto es el desarrollo de manera cooperativa de un juego de mesa en entorno texto mediante la utilización de todas las herramientas aprendidas hasta el momento en **Python**.  
El verdadero reto del juego es que sea **funcional**, es decir, que se pueda jugar con el resultado de ganar o perder partidas contra una inteligencia artificial muy básica por parte del ordenador. No hace falta el uso de una interfaz gráfica para poder jugarlo, sino que directamente desde la consola se puede jugar.  
El juego que hemos decidido desarrollar es el ***Timbiriche***, también es conocido como _Dots and Boxes_ o _Juego de los Cuadrados_ en algunos lugares.

---

# Cómo jugar al timbiriche (2 personas)!!!

### **1. Preparación**

    1.1 Se elige el tamaño del tablero.
  
    1.2 Se elige el primer turno de forma aleatoria.
  
### **2. Jugar turnos**

    2.1 El jugador que tiene el turno primero traza una línea entre dos puntos.
  
    2.2 El siguiente jugador también traza una línea entre dos puntos.
  
    2.3 Si al trazar una línea, se cierra un cuadrado, el jugador que lo ha cerrado lo marca con su color.
  
    2.4 El jugador que ha cerrado el cuadrado tiene el turno en la próxima jugada.
  
    2.5 El objetivo del juego es cerrar el mayor número de cuadrados posibles.

### **3. Finalizar la partida**
    3.1 La partida finaliza cuando no se pueden trazar más líneas.
  
    3.2 Gana el jugador que haya conseguido marcar más cuadrados en el proceso.

### **4. Reglas adicionales**
  - Si el jugador no puede trazar una línea, pierde el turno.
  - Si un jugador cierra un cuadrado y tiene la oportunidad de cerrar otro en el mismo turno, puede hacerlo.


### Estrategias

- Es importante tratar de cerrar cuadrados y evitar que tus oponentes los cierren.
- Piensa bien el lugar donde poner la línea para poder hacer el máximo número de puntos de una sola vez.
- Si la única opción es poner una línea donde tu rival puede obtener puntos, céntrate ponerla para que haga el mínimo posible.
- Tienes que estar muy atento, que no se te escape cerrar ningún cuadrado.



# Creación del documento PCE

## Errores en las pruebas unitarias e integradas

### Fallo:
- Se puede introducir una misma línea más de 1 vez

### Solución:
- Poner una condición de que si ya hay una línea en las coordenadas introducidas, se imprima un error y vuelva a pedir una línea que no haya sido introducida.

### Fallo: 
- Error al verificar cuadrados sobre las líneas de los bordes (por ejemplo, al poner una línea al borde izquierdo verifica si se ha formado cuadrados en la izquierda y en la derecha cuando en su izquierda no se puede formar un cuadrado)

### Solución:
- Poner condicionales elif de sí la coordenada introducida es altura y = 0 verifique solo el cuadrado de abajo, si x = 0 verifique solo el cuadrado derecho, si y = n(el tamaño del casillero) - 1 verifique solo el cuadrado de arriba, si x = n - 1 verifique solo el cuadrado izquierdo.

### Fallo: 
- Se puede introducir coordenadas de 2 puntos que no son cercanos o que forman diagonales o 2 puntos con las mismas coordenadas

### Solución:
- Añadimos un condicional else en caso de que los puntos no sean cercanos y formen una línea vertical u horizontal y añadimos un error_coordenadas =True para que se salte varias líneas de código con error_coordenadas = False (como las de imprimir el marcador y el de cambiar el turno del jugador X) y vuelva a pedirme coordenadas nuevamente.

### Fallo:
- Al poner una línea y cerrar a la vez 2 cuadrados el programa te lo cuenta con un punto y solo pone una inicial en un cuadrado

### Solución:
- Añadimos otros condicionales elif que verifique sobre esa línea si ha cerrado 2 cuadrados de 2 puntos y ponga tus 2 iniciales sobre los 2 cuadrados.

### Fallo:
- ValueError al introducir caracteres o solo una parte de las coordenadas sin querer al pedir las coordenadas o en el tamaño del casillero

### Solución:
- Si se introduce caracteres o has escrito mal las coordenadas o el tamaño del casillero, hemos introducido try except para que me vuelva a pedir otra vez las coordenadas y en el tamaño del casillero lo mismo

### Fallo:
- IndexError al introducir coordenadas fuera del rango 

### Solución:
- Dentro del try except hemos añadido un condicional if para que las coordenadas si están fuera del rango permitido nos vuelva a pedir otra vez las coordenadas de un punto
