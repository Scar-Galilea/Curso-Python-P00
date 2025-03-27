"""
Nombre: Galilea Peralta Contreras.
Fecha: 11 de marzo del 2025.

Descripción:
Crea una clase llamada Personaje que simule los movimientos de un personaje de videojuegos en una ventana.

1. El personaje se moverá por una ventana de tamaño máximo (x, y) = (10, 10) y podrá realizar los siguientes movimientos si no supera el límite de la ventana:
      * Avanzar (caracteres 'A' o 'a'): aumenta en 1 la posición en y,
      * Retroceder (caracteres 'R' o 'r'): disminuye en 1 la posición en y,
      * Derecha (caracteres 'D' o 'd'): aumenta en 1 la posición en x,
      * Izquierda (caracteres 'I' o 'i'): disminuye en 1 la posición en x.

2. El personaje tendrá los siguientes métodos (además de los métodos mágicos):
      * moverse() que recibe la orden como parámetro,
      * posicion_actual() que muestra en consola la posición en (x,y).

3. Se debe llevar un registro del ID de los personajes creados, por lo que se debe utilizar un atributo de clase.

4. Al crear los objetos de la clase, inicialmente deben establecerse en el origen (x, y) = (0, 0).

5. Se debe solicitar iterativamente la secuencia de movimientos e indicar la posición final de la secuencia.

6. El programa se detendrá con los caracteres 'S' o 's'.

"""

# Clase que representa un personaje.
class Personaje:
    contador_id = 1
    def __init__(self):
        # Posición inicial del personaje en (0,0)
        self.x = 0
        self.y = 0
        # Asignación de un ID a cada personaje.
        self.contador_id  = Personaje.contador_id
        Personaje.contador_id += 1

    def moverse(self,ordenes : str) -> None:
        """
        Mueve el personaje según las órdenes proporcionadas.
        :param ordenes: Cadena de caracteres que representa los movimientos.
        """
        ordenes = ordenes.lower()
        for i in ordenes:
            # Avanzar
            if i == 'a' and self.y != 10:
                self.y += 1
            # Retroceder
            elif i == 'r' and self.y != 0:
                self.y -= 1
            # Derecha
            if i == 'd' and self.x != 10:
                self.x += 1
            # Izquierda
            elif i == 'i' and self.x != 0:
                self.x -= 1

    def posicion_actual(self) -> None:
        """
        Imprime la posición actual del personaje en el formato (x, y).
        """
        print(f"Posición actual: (x,y) = ({self.x}, {self.y}).")

    def __str__(self) -> str:
        """
        Retorna una representación en cadena del objeto Personaje.
        """
        return f"Personaje  ( id = {self.contador_id}, x: {self.x}, y: {self.y}.)"


def main() -> None:
    """
    Función principal.
    """
    b = None
    print("-- Se crea el objeto e la clase Personaje y se imprime.")
    jugador = Personaje()
    print(jugador)
    print()
    print(  "Se solicitan interactivamente una secuencias de movimiento.")

    # Bucle para solicitar movimientos hasta que se ingrese 's' o 'S'.
    while b != "s":
        # Al asignarle lower permite que todos los caracteres los tome como minuscula.
        # Esto ayuda que se disminuya menos código al estar velicando si es minuscula o no.
        b = input("Ingresa las órdenes de movimiento: ").lower()

        jugador.moverse(b)
        jugador.posicion_actual()
    print()
    print("Fin del programa.")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()

