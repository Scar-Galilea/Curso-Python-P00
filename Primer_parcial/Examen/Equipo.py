"""
Nombre: Galilea Peralta Contreras.
Fecha: 02 de abril del 2025.

Descripción:
"""

from Jugador import Jugador

class Equipo:
    no_id = 1
    def __init__(self,nombre:str, *jugadores:tuple[Jugador]):
        Equipo.no_id += 1
        self._nombre = nombre
        self._jugadores = list(jugadores)
        self._id_equipo = int(Equipo.no_id)

    def agregar_jugadores(self,*jugadores: Jugador) -> None:
        for jugador in jugadores:
            if jugador != self._jugadores:
                self._jugadores.append(jugador)
            else:
                print(f"El jugador {jugador} forma parte del equipo {self.nombre}.")

    def eliminar_jugadores(self, *jugadores: Jugador) -> None:
        for jugador in jugadores:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)
            else:
                print(f"El jugador {jugador} no forma parte del equipo {self.nombre}.")

    def mostrar_jugadores(self) -> None:
        print(f"*** Lista de jugadores del equipo de {self.nombre} ***")
        for jugador in self._jugadores:
            print(jugador)



    # Métodos de acceso para obtener atributos encapsulados.
    @property
    def nombre(self) -> str:
        return self._nombre
    @property
    def id_equipo(self) -> int:
        return self._id_equipo

    # Métodos modificadores (setter) para cambiar valores de los atributos encapsulados.
    @nombre.setter
    def nombre(self, nombre : str) -> None:
        self._nombre = nombre

    def __str__(self) -> str:
        pass
        #return f"Jugador (Nombre: {self._nombre},  Numero: ({self._j}), goles = {self._goles})"


def main() -> None:
    """
    Función principal.
    """



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()