"""
Nombre: Galilea Peralta Contreras.
Fecha: 02 de abril del 2025.

Descripción:

"""

class Jugador:
    def __init__(self,nombre: str,numero: int, goles: int = 0):
        self._nombre = nombre
        self._numero = numero
        self._goles = goles

    def anotar_goles(self,no_goles: int) -> None:
        self._goles += no_goles

    # Métodos de acceso para obtener atributos encapsulados.
    @property
    def nombre(self) -> str:
        return self._nombre
    @property
    def numero(self) -> int:
        return self._numero
    @property
    def goles(self) -> int:
        return self._goles

    # Métodos modificadores (setter) para cambiar valores de los atributos encapsulados.
    @nombre.setter
    def nombre(self, nombre : str) -> None:
        self._nombre = nombre
    @numero.setter
    def numero(self, numero: int) -> None:
        self._numero = numero
    @goles.setter
    def goles(self, goles: int) -> None:
        self._goles = goles


    def __str__(self) -> str:
        return f"Jugador (Nombre: {self._nombre},  Numero: ({self._numero}), goles = {self._goles})"

def main() -> None:
    """
    Función principal.
    """


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()