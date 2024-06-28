# Juegos en Python

## ¿De que trata este repositorio?
Este repositorio se intenta plantear mini proyectos para que otras personas 
que se inicien en este lenguaje puedan practicar e intentar hacerlos.

## Enunciados:
1. [Calculadora Simple](#calculadora-simple)
2. [Ahorcado](#ahorcado)
3. [Dungeon Magic](#dungeon-magic)

## Calculadora Simple
Realiza una calculadora que contenga el siguiente menu:
1) Suma
2) Resta
3) Multiplicaión
4) División
5) Factorial
6) Potencia
7) Es primo?.
8) Salir

Hasta que el usuario no le de a "Salir" no se terminará el programa.
En cada operación se pedirán al usuario que introduzca dos números salvo en el
"Factorial" y en el "Es primo?", en esos casos solo se le introducirán un número.
Además en el "Es primo?" deberá de comprobar y mostrar si es primo o no lo es.

## Ahorcado
Recrea el Juego del ahorcado, el juego será de dos jugadores. Uno escribe la 
palabra (ojo solo quiero una palabra, pero si te quieres complicar más puedes hacerlo de varias) 
y el otro acierta. Cuando empieze el juego deverá de aparecer la palabra escondida con guiones bajos "_"
y con un espacio en cada letra.

El personaje completo sería este: print("-----\n|   |\n|   O  \n| --|--\n|   |\n|  / \ ")

Ayuda: El juego requiere recorrer <a href="https://ellibrodepython.com/cadenas-python" target="_blank">cadenas</a>.

## Dungeon Magic
Crea un juego rpg por turnos, serás un heroe que te dan a elegir al inicio 3 clases diferentes que serán:

1) Guerrero -> 200 de vida y 50 de daño.
2) Mago -> 150 de vida y 60 de daño.
3) Picaro -> 180 de vida y 55 de daño.

Cada clase tiene un ataque normal y 2 habilidades especiales que son:

1) Para el guerrero -> Golpe de espada: 15% más de daño y Ataque de furia: 20% más de daño.
2) Para el mago -> Bola de fuego: 20% más de daño y Rayo de hielo: 45% más de daño.
3) Para el picaro -> Estocada: 18% más de daño y Ataque sorpresa: 30% más de daño.

Las habilidades fuertes solo se podrán utilizar 3 veces por cada 2 combates, las habilidades superfuertes 
solo se podrán utilizar 2 veces por cada 2 combates y los escudos solo habrá 2 por
cada 2 combates. Al acabar el 2 combate el héroe se curará un 58% de la vida que tengan en ese 
momento y a demás se reiniciarán las habilidades especiales y el escudo.

Los enemigos son:

1) Dragón: 200 de vida y 50 de daño.
2) Liche: 170 de vida y 40 de daño.
3) Orco: 150 de vida y 30 de daño.
4) Esqueleto: 100 de vida y 20 de daño.
5) Goblin: 80 de vida y 15 de daño.

Los enemigos podrán fallar ataques (yo dejé al azar que eligiera cuando fallan), tambien los enemigos solo 
pueden hacer un ataque normal (pero si quieres complicarlo más le puedes poner ataques especiales también).

Una vez acabado la partida sea ganada o perdida, se preguntará al usuario si quiere volver a 
jugar o no.

Ayuda: Para este juego es necesario saber como van las clases <a href="https://ellibrodepython.com/programacion-orientada-a-objetos-python">documentación</a>
y <a href="https://www.youtube.com/watch?v=JVNirg9qs4M&t=535s">video</a>.