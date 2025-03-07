"""
Nombre: Galilea Peralta Contreras.
Fecha: 05 de marzo del 2025.

Descripción:

"""
from socket import send_fds


class Estudiante:
    def __init__(self, nombre: str):
        # Asignar la variable como un objeto.
        self.nombre = nombre
        self.temas_aprendidos = []

    def aprender_temas(self,tema:str) -> None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")


class Profesor:
    def __init__(self,nombre: str):
        self.nombre = nombre
        self.temas_aprendidos = []

    def dominar_tema(self,tema:str) -> None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} dominó {tema}")

    def enseñar_tema(self,no_tema: int) -> None:
        print(f"{self.nombre} enseñó {no_tema} de temas")


def main() -> None:
    """
    Función principal.
    """


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
