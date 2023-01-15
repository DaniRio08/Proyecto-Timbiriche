# Proyecto Juego Timbiriche
##### Por Dani Río y Raúl Velásquez
---
### Objetivos
El objetivo de este proyecto es el desarrollo de manera cooperativa de un juego de mesa en entorno texto mediante la utilización de todas las herramientas aprendidas hasta el momento en **Python**.  
El verdadero reto del juego es que sea **funcional**, es decir, que se pueda jugar con el resultado de ganar o perder partidas contra una inteligencia artificial muy básica por parte del ordenador. No hace falta el uso de una interfaz gráfica para poder jugarlo, sino que directamente desde la consola se puede jugar.  
El juego que hemos decidido desarrollar es el ***Timbiriche***, también es conocido como _Dots and Boxes_ o _Juego de los Cuadrados_ en algunos lugares.

---

# Reglas del Juego

El ***Timbiriche*** o (_Dots and Boxes_) es un juego de mesa para dos o más jugadores, en este caso jugará el usuario contra el ordenador.  
El objetivo del juego es conectar puntos en un tablero de la dimensión que se desee. 
Los turnos consisten en que cada jugador dibuja una línea entre dos puntos adyacentes del tablero, cuando al dibujar la línea se complete un cuadrado ese jugador obtiene un punto y tiene otro turno, por lo que puede dibujar otra línea. El juego termina cuando no haya más líneas por poner. Y gana quién haya conseguido completar más cuadrados.

### Ejemplo de una partida
1. Se decide la dimensión del tablero. Y se empieza a jugar estando este vacío, sin ninguna línea.
2. El primer jugador elige un punto cualquiera del tablero y conecta dos puntos adyacentes con una línea.
3. Los jugadores continúan turnándose para conectar puntos adyacentes con líneas.
4. Si un jugador logra conectar dos líneas de forma tal que se cierra un cuadrado, este jugador recibe un punto y puede continuar jugando.
5. El juego termina cuando no quedan más puntos por conectar o cuando los jugadores acuerdan finalizarlo.
6. El jugador con más puntos al final del juego, gana.

### Estrategias

- Es importante tratar de cerrar cuadrados y evitar que tus oponentes los cierren.
- Piensa bien el lugar donde poner la línea para poder hacer el máximo número de puntos de una sola vez.
- Si la única opción es poner una línea donde tu rival puede obtener puntos, céntrate ponerla para que haga el mínimo posible.
- Tienes que estar muy atento, que no se te escape cerrar ningún cuadrado.
