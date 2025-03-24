"""
Nombre: Galilea Peralta Contreras.
Fecha: 24 de marzo del 2025.

Descripción:

"""
from Ej2_Scoreboard import Scoreboard

class Window:
    def __init__(self,text: str, width: int, height: int, scoreboard: Scoreboard = Scoreboard()):

    def __str__(self) -> str:
        return f"Empleado  ( Id = {self.no_id}. Nombre: {self.nombre}. Sueldo: {self.sueldo})"


def main() -> None:
    """
    Función principal.
    """


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
