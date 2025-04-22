"""
Nombre: Galilea Peralta Contreras.
Fecha: 02 de abril del 2025.

Descripción:
Se desea desarrollar un sistema en Python para gestionar un torneo de fútbol en el que participan varios equipos, y cada equipo está compuesto por jugadores. El sistema debe considerar lo siguiente:

1. Gestionar Jugadores:
Cada jugador tiene un nombre, un número y una cantidad de goles anotados.
Los jugadores pueden anotar goles, y el sistema debe actualizar su contador de goles.
Los atributos de los jugadores deben estar protegidos, y se debe controlar el acceso a ellos mediante métodos de acceso.
"""

class Jugador:
    def __init__(self,nombre: str,numero: int, goles: int = 0):
        """
        Constructor de la clase Jugador.
        :param nombre: Nombre del jugador.
        :param numero: Número del jugador en el equipo.
        :param goles: Cantidad de goles anotados (por defecto es 0).
        """
        self._nombre = nombre
        self._numero = numero
        self._goles = goles

    def anotar_goles(self,no_goles: int) -> None:
        """
        Incrementa el número de goles anotados por el jugador.
        :param no_goles: Cantidad de goles a sumar al total.
        """
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
        """
        Devuelve una representación en cadena del jugador.
        :return: Cadena con la información del jugador.
        """
        return f"Jugador (Nombre: {self._nombre},  Numero: ({self._numero}), goles = {self._goles})"

def main() -> None:
    """
    Función principal.
    """


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()