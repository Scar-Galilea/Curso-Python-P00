"""
Nombre: Galilea Peralta Contreras.
Fecha: 11 de marzo del 2025.

Descripción:

"""

class Personaje:
    contador_id = 1
    def __init__(self):

        self.x = int
        self.y = int
        self.contador_id  = Personaje.contador_id
        Personaje.contador_id += 1

    def moverse(self,ordenes : str) -> None:
        """
        Se utiliza para aumentar el sueldo de acuerdo con un porcentaje.
        :param ordenes: Porcentaje a incrementar el sueldo.
        """
        acumulador_x = 0
        acumulador_y = 0

        for i in ordenes.lower():
            if i == 'a':
                acumulador_y += 1
            elif i == 'r' and acumulador_y != 0:
                acumulador_y -= 1
            if i == 'd':
                acumulador_x += 1
            else:
                if i == 'i' and acumulador_x != 0:
                    acumulador_x -= 1



    def __str__(self) -> str:
        return f"Personaje  ( Id = {self.contador_id}, x: {self.x}, y: {self.y}.)"


def main() -> None:
    """
    Función principal.
    """


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()

