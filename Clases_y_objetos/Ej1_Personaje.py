"""
Nombre: Galilea Peralta Contreras.
Fecha: 11 de marzo del 2025.

Descripción:

"""

class Personaje:
    contador_id = 1
    def __init__(self):

        self.x = 0
        self.y = 0
        self.contador_id  = Personaje.contador_id
        Personaje.contador_id += 1

    def moverse(self,ordenes : str) -> None:
        """
        Se utiliza para aumentar el sueldo de acuerdo con un porcentaje.
        :param ordenes: Porcentaje a incrementar el sueldo.
        """
        ordenes = ordenes.lower()
        for i in ordenes:
            if i == 'a' and self.y != 10:
                self.y += 1
            elif i == 'r' and self.y != 0:
                self.y -= 1
            if i == 'd' and self.x != 10:
                self.x += 1
            elif i == 'i' and self.x != 0:
                self.x -= 1

    def posicion_actual(self) -> None:
        print(f"Posición actual: (x,y) = ({self.x}, {self.y}).")

    def __str__(self) -> str:
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
    while b != "s":
        b = input("Ingresa las órdenes de movimiento: ").lower()
        jugador.moverse(b)
        jugador.posicion_actual()
    print()
    print("Fin del programa.")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()

