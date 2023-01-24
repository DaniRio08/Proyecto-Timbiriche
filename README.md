# Proyecto Juego Timbiriche
##### Por Dani Río y Raúl Velásquez
---
## Objetivos
El objetivo de este proyecto es el desarrollo de manera cooperativa de un juego de mesa en entorno texto mediante la utilización de todas las herramientas aprendidas hasta el momento en **Python**.  
El verdadero reto del juego es que sea **funcional**, es decir, que se pueda jugar con el resultado de ganar o perder partidas contra una inteligencia artificial muy básica por parte del ordenador. No hace falta el uso de una interfaz gráfica para poder jugarlo, sino que directamente desde la consola se puede jugar.  
El juego que hemos decidido desarrollar es el ***Timbiriche***, también es conocido como _Dots and Boxes_ o _Juego de los Cuadrados_ en algunos lugares.

---

## IDC (Investigación y desarrollo conceptual)

Elegimos el Timbiriche para hacer el proyecto porque es un juego que nos era familiar tanto a Raúl como a mí y pensamos que se adaptaba correctamente a las características que pedía el trabajo. Aun así, para refrescar un poco las reglas nos estuvimos informando y jugando algunas partidas entre nosotros. También miramos ejemplos del juego online para ver como funcionaban.

### Cómo jugar al Timbiriche
El ***Timbiriche*** o (_Dots and Boxes_) es un juego de mesa para dos o más jugadores, en este caso se podrá jugar entre dos jugadores así como contra el ordenador.  
El objetivo del juego es conectar puntos en un tablero de la dimensión que se desee. 
Los turnos consisten en que cada jugador dibuja una línea entre dos puntos adyacentes del tablero, cuando al dibujar la línea se complete un cuadrado ese jugador obtiene un punto y tiene otro turno, por lo que puede dibujar otra línea. El juego termina cuando no haya más líneas por poner. Y gana quién haya conseguido completar más cuadrados.

**1. Preparación**

    1.1 Se elige el tamaño del tablero, cuanto más grande, más difícil y más durará la partida.
    
    1.2 Cada jugador elige la inicial con la que quiere identificarse, esta aparecerá en el centro del cuadrado cuando se consiga un punto.
    
    1.3 Se elige el primer turno de forma aleatoria.
  
**2. Jugar turnos**

    2.1 El jugador que tiene el turno primero traza una línea entre dos puntos contiguos.
  
    2.2 El siguiente jugador hace lo mismo.
  
    2.3 Si al trazar una línea, se cierra un cuadrado, el jugador que lo ha cerrado consigue un punto y pone su letra en el cuadrado para indicarlo.
  
    2.4 Cuando se cierra un cuadrado y, por lo tanto, se consigue un punto, ese jugador vuelve a tener un turno.
  
    2.5 El objetivo del juego es cerrar el mayor número de cuadrados posibles.

**3. Finalizar la partida**

    3.1 La partida finaliza cuando no se pueden trazar más líneas.
  
    3.2 Gana el jugador que haya conseguido cerrar más cuadrados.

**4. Estrategias**

    4.1 Es importante tratar de cerrar cuadrados y evitar que tus oponentes los cierren.
    
    4.2 Piensa bien el lugar donde poner la línea para poder hacer el máximo número de puntos de una sola vez al encadenar turnos.
    
    4.3 Si la única opción es poner una línea donde tu rival puede obtener puntos, céntrate ponerla para que haga el mínimo posible.
    
    4.4 Tienes que estar muy atento, que no se te escape cerrar ningún cuadrado.
    
---

## TEP (Traslado a Entorno de Programa)

**Petición de información al usuario.**
(variables que influyen en cómo funciona la partida)
~~~
- El usuario indica si quiere jugar contra la IA o contra otro jugador.
- Petición de iniciales con las cuales los jugadores se quieren identificar.
- Se elige de forma random quién comienza la partida.
- Por último, el usuario elige el tamaño del casillero con el que quiere jugar.
~~~

**Funciones para preparar la partida.**

~~~
- Funciones para verificar si se ha formado un cuadrado. (2 funciones)
        - Una línea horizontal solo permite cerrar el cuadrado de arriba y el de abajo.
        - Una línea vertical permite cerrar el cuadrado de su izquierda y el de la derecha.
- Función que cuenta cuantas líneas hay entre cuatro puntos del tablero (se usa para determinar donde dibuja la línea la "IA").
- Bucle que crea el casillero del tamaño elegido por el usuario anteriormente.
- Función para imprimir el casillero con un bucle.
- Se define una lista de todos los movimientos posibles.
- Se llena la lista de movimientos con un bucle.
- La variable finalizar_partida se determina como False
~~~

**Turnos.**

~~~
- Se establece un bucle dónde se gestionan los turnos. Este continúa mientras queden líneas por poner.
- Si es el turno del Jugador1: se muestra la interacción del Jugador1.
- En el caso de que al inicio se haya decidido que la partida es entre dos jugadores: se muestra la interacción del Jugador 2(=Jugador1).
- En el caso de que al inicio se haya decidido que la partida se juega contra el ordenador: se muestra la interacción de la "IA".
~~~

**Interacción del Jugador1 o Jugador 2**

~~~
- En caso de ser el primer turno se ve la impresión del tablero vacío.
- En caso de no ser el primer turno se ve la situación actual del tablero.
- Se informa por pantalla de si el turno le pertenece al Juagador1 o al Jugador2
- Se piden las coordenadas del primer punto del tablero (x1 y1).
- Se piden las coordenadas del segundo punto del tablero (x2 y2).
- Se volverán a pedir las coordenadas sin pasar el turno en el caso de que no sean válidas:
        - Porque la línea ya esté dibujada
        - Porque los puntos introducidos no sean contiguos
        - Porque las coordenadas estén fuera del rango del casillero
        - Porque haya habido un error de sintaxis al escribirlas
- En el caso de que las coordenadas sean válidas el turno continúa.
- Se llaman a las funciones que verifican si se ha completado un cuadrado.
- Si al dibujar la línea esta no completa un cuadrado:
        - Se muestra por pantalla el casillero con la línea dibujada.
        - Se establece que el siguiente turno será del otro jugador.
- Si al dibujar la línea se completa un cuadrado:
        - Se muestra por pantalla el casillero con la línea dibujada y la inicial del Jugador en el centro del cuadrado.
        - Se muestra un mensaje de que el jugador ha conseguido un punto.
        - Se establece que el siguiente turno volverá a ser de este jugador.
- Si el turno era del Jugador1, se elimina su movimiento realizado de la lista de movimientos posibles para que si juega contra la "IA" esta no lo pueda tener en cuenta.
- Se comprueba que la partida no haya finalizado.
- Se muestra por pantalla el marcador con las puntuaciones actuales de cada jugador.
~~~

**Interacción de la "IA"**

~~~
- Con un bucle la "IA" recorre la lista con todos los movimientos disponibles.
- Para cada movimiento de la lista se llama a la función que verifica cuantas líneas del cuadrado hay actualmente antes de poner la línea que dibujaría el movimiento. Pueden ser 0, 1, 2 o 3 líneas.
- Dependiendo del resultado de la función llamada anteriormente, cada movimiento se almacena en una nueva lista. Hay 3 listas:
        - Una para almacenar los movimientos que pondrían la 1ª o 2ª línea del cuadrado
        - Una para almacenar los movimientos que pondrían la 3ª línea del cuadrado
        - Una para almacenar los movimientos que pondrían la 4ª línea del cuadrado
- De las tres listas resultantes se prioriza que la jugada de la "IA" sea una que complete un cuadrado, por lo tanto si la lista no está vacía se elige de manera aleatoria movimiento de esta.
- Si no hay ningún movimiento que complete un cuadrado, la jugada de la "IA" se elegirá de manera aleatoria de entre uno de los movimientos de la lista que pondría la 1ª o 2ª línea del cuadrado, ya que no hace que el rival pueda conseguir punto.
- En el caso de que las otras dos listas estén vacías, la única opción restante es un movimiento de la lista que pondría la 3ª línea del cuadrado.
- Una vez elegida la jugada que va a hacer la "IA" muestra por pantalla cuál será.
- Se llaman a las funciones que verifican si se ha completado un cuadrado.
- Si al dibujar la línea esta no completa un cuadrado:
        - Se muestra por pantalla el casillero con la línea dibujada.
        - Se establece que el próximo turno será para el Jugador1.
- Si al dibujar la línea se completa un cuadrado:
        - Se muestra por pantalla el casillero con la línea dibujada y la inicial del ordenador en el centro del cuadrado.
        - Se muestra un mensaje de que el ordenador ha conseguido un punto.
        - Se establece que el siguiente turno volverá a ser del ordenador.
- Se imprime por pantalla el marcador con la puntuación actual de la "IA" y del Jugador1.
- Se vuelven a definir las listas donde se almacenan los movimientos dependiendo de cuantas líneas tenga el cuadrado para que vuelvan a estar vacías para el próximo turno.
- Se elimina la jugada realizada de la lista de movimientos posibles.
- Se comprueba que la partida no haya finalizado.
~~~

**Terminar la partida**

~~~
- Una vez la variable finalizar_partida deja de ser False, se rompe el bucle del juego.
- Si la partida ha sido entre Jugador1 y Jugador2:
        - Si los puntos del Jugador1 son mayores que los del Jugador2: Se muestra un mensaje por pantalla de victoria del Jugador1
        - Lo mismo, pero por victoria del Jugador2.
        - Puede haber empate, por lo que se muestra un mensaje de empate.
- Si la partida ha sido entre Jugador1 y la "IA":
        - Si los puntos del Jugador1 son mayores que los de la "IA": Se muestra un mensaje por pantalla de enhorabuena al Jugador1 por ganar al ordenador.
        - En caso de que la "IA" haya conseguido más puntos que el Jugador1: Se muestra un mensaje de que el Jugador1 ha perdido.
        - Puede haber empate, por lo que se muestra un mensaje de empate.
~~~

---

## CCF (Codificación y Creación de Funciones)

Lo primero que hicimos para poder empezar a programar el juego fue pensar en como crear el casillero del Timbiriche. Y es que este es la parte principal del juego, ya que este es el mismo cada turno, pero se va actualizando con las diferentes líneas y letras que se pueden dibujar en él. Así que creamos una lista de listas donde cada elemento de la lista es una fila del casillero y cada elemento de la sublista representa un punto del tablero. Además de esta manera se podía imprimir de forma sencilla con un bucle "for".

Al ya tener un casillero, el siguiente paso fue pensar en como podíamos modificarlo para poder añadir líneas donde quisiéramos. Ejemplo de como modificar el casillero: casillero[posición de la lista][posición de la sublista]=["-","-","-"] → línea horizontal

Después hicimos la parte del código que se encargaba de que se pudiesen introducir coordenadas de forma sencilla para que uniesen dos puntos del casillero con una línea, igual que explicamos antes. El problema fue que internamente el casillero no tenía 4 filas y 4 columnas, que eran los puntos que se mostraban por pantalla, por lo que había que hacer una conversión entre los valores que se introducen y los que representan en realidad dentro de la lista de listas. Y también tuvimos que tener en cuenta que era diferente introducir una línea horizontal a una vertical, por lo que tuvimos que crear un par de condiciones que evaluasen si las coordenadas introducidas representaban una línea horizontal o vertical para poder dibujarlas de diferentes maneras.

Una vez con todo esto listo, ya podíamos seguir avanzando con el proyecto. Lo siguiente fue declarar todas las variables para poder jugar una partida y también importar bibliotecas que añadiesen características chulas a nuestro proyecto como random, colorama o time.

El siguiente paso fue crear funciones que sirviesen para verificar si al poner la línea se cerraba un cuadrado. Llegamos a la conclusión de que al poner una línea no hacía falta verificar si se cerraban todos los cuadrados, sino que solo hacía falta comprobar 2. Cuando se introduce una línea horizontal, esta solo puede cerrar el cuadrado que se sitúa arriba de ella o el de abajo, mientras que una línea vertical solo puede cerrar el cuadrado de su derecha o de su izquierda.
La función para verificar si se ha cerrado un cuadrado funciona de la siguiente manera: primero se modifican las coordenadas introducidas por el usuario para situarse en el punto central de los cuadrados que se tienen comprobar, y una vez hecho eso se comprueba si sus puntos de alrededor no están vacíos. En el caso de que eso se cumpla significa que el cuadrado se ha cerrado.

Una vez teniendo una forma de comprobar si se hace un cuadrado, programamos que usando esas funciones se llevase la puntuación y los turnos de la partida. Cuando se cierra un cuadrado, el jugador suma un punto y mantiene el turno, mientras que, por el contrario, si no cierra un cuadrado, el turno pasa al otro jugador. Tamibién usamos la puntuación como la forma de determinar si la partida había acabado, cuando la puntuación entre los dos jugadores fuese igual al máximo número de puntos obtenibles.

Posteriormente, programamos toda la interacción del Jugador2, que al fin y al cabo era muy similar a la parte del Jugador1. Y es que aunque la idea del proyecto era que se pudiese jugar contra una "IA" muy básica, decidimos dejar esa parte para el final, para hacerla cuando tuviésemos muy claro como funcionaba todo el juego.

Nos propusimos que el juego sería mucho más entretenido para el jugador si se le daban ciertas opciones para elegir al comienzo del juego. Así que escribimos al principio del programa un poco de código con el cual el jugador pudiese interactuar decidiendo como se quería identificar al jugar y de qué tamaño quería que fuese el casillero, entre otras cosas

Posteriormente, corregimos ciertos errores que habíamos ido encontrando en el código al ir probando el juego. Muchos de ellos surgían a la hora de introducir las coordenadas para decidir la línea que se quería dibujar. Por ejemplo, se podía introducir dos veces la misma línea, lo que provocaba que el jugador perdiese turno sin hacer ningún avance en el casillero. También si se introducían las coordenadas de forma errónea o fuera del rango saltaba un ValueError o IndexError que hacían que no se pudiese continuar la partida y se tuviese que volver a empezar desde cero. Para corregir estos usamos un try/except. También por algunos problemas de tabulación no se mostraba el mensaje de finalización de partida al acabar el juego.

Una vez tuvimos un programa con el que ya se podía jugar una partida entre dos personas, nos pusimos a estudiar como hacer que fuese posible jugar contra una "IA" muy básica.
La "IA" la programamos de la siguiente manera: 
* Primero creamos una lista que se llenaba de todos los movimientos posibles dependiendo del tamaño de casillero elegido con un bucle. Consideramos un movimiento el uso de dos coordenadas para unir dos puntos del casillero.
* Una vez hecho, eso durante el turno de la "IA" programamos que se recorra esa lista con todos los movimientos actuales con un bucle for.
* Creamos una función que verifica cuantas líneas hay ya dibujadas en el casillero en los cuadrados que podría cerrar la línea que se dibujaría con el movimiento. Antes de dibujar esta línea puede haber o bien 0 líneas, 1 línea, 2 líneas o 3 líneas ya dibujadas. Cada una se contempla con una condición dentro de la función.
* Por lo tanto, para cada movimiento de la lista de movimientos actuales se verifica que pasaría si se pone esa línea. Y dependiendo del resultado, ese movimiento se almacena en tres listas distintas. La primera lista almacena los movimientos que pondrían la 1ª o 2ª línea del cuadrado, la segunda lista almacena los movimientos que pondrían la 3ª línea y la tercera lista contiene los movimientos que cierran cuadrados.
* Posteriormente, programamos un condicional que tenga en cuenta si la lista de movimientos que cierran un cuadrado está vacía o no, ya que si no lo está queremos que la "IA" priorice uno de esos movimientos. En el caso de que esté vacía, la siguiente mejor opción es que la "IA" ponga la primera o segunda línea del cuadrado, puesto que no supondría que el rival pueda hacer un punto. Por último, en el caso de que las otras dos listas estén vacías, no queda otra opción que la "IA" elija un movimiento que pone la tercera línea de un cuadrado, lo que supondrá que el rival pueda conseguir un punto.
* Lo siguiente fue programar que la jugada elegida se ejecute como un turno normal, al igual que los turnos del Jugador1 y Jugador2, haciendo que se compruebe si con la línea dibujada se forma un cuadrado y, por lo tanto, sumando un punto y manteniendo el turno de la "IA".

Finalmente, lo único que quedaba por programar eran algunas correcciones estéticas a la hora de que el juego se viese más claro por la consola. Y a su vez que el programa también fuese más entendible añadiendo y mejorando algunos comentarios.

---

## PCE (Pruebas y Corrección de Errores)

### Fallo:
- Se puede introducir una misma línea más de 1 vez.

### Solución:
- Poner una condición de que si ya hay una línea en las coordenadas introducidas, se imprima un error y vuelva a pedir una línea que no haya sido introducida.

### Fallo: 
- Error al verificar cuadrados sobre las líneas de los bordes (por ejemplo, al poner una línea al borde izquierdo verifica si se ha formado cuadrados en la izquierda y en la derecha cuando en su izquierda no se puede formar un cuadrado), que hacen que salte un IndexError out of range.

### Solución:
- Poner condicionales elif donde si la coordenada introducida es altura y = 0 verifique solo el cuadrado de abajo, si x = 0 verifique solo el cuadrado derecho, si y = n(el tamaño del casillero) - 1 verifique solo el cuadrado de arriba, si x = n - 1 verifique solo el cuadrado izquierdo.

### Fallo: 
- Se puede introducir coordenadas de 2 puntos que no son contiguos o que forman diagonales o 2 puntos con las mismas coordenadas.

### Solución:
- Añadimos un condicional else en caso de que los puntos no sean cercanos y formen una línea vertical u horizontal y añadimos un error_coordenadas =True para que se salte varias líneas de código con error_coordenadas = False (como las de imprimir el marcador y el de cambiar el turno del jugador X) y vuelva a pedir las coordenadas nuevamente.

### Fallo:
- Al poner una línea y cerrar a la vez 2 cuadrados el programa te lo cuenta con un punto y solo pone una inicial en un cuadrado.

### Solución:
- Añadimos otros condicionales elif que verifique sobre esa línea si ha cerrado 2 cuadrados de 2 puntos y ponga la inicial sobre los 2 cuadrados.

### Fallo:
- ValueError al introducir caracteres o solo una parte de las coordenadas por equivocación al pedir las coordenadas o en el tamaño del casillero.

### Solución:
- Si se introducen caracteres o se han escrito mal las coordenadas o el tamaño del casillero, hemos introducido try except para que me vuelva a pedir otra vez las coordenadas y en el tamaño del casillero lo mismo.

### Fallo:
- IndexError al introducir coordenadas fuera del rango 

### Solución:
- Dentro del try except hemos añadido un condicional if para que las coordenadas si están fuera del rango permitido se vuelva a pedir otra vez las coordenadas de un punto.
