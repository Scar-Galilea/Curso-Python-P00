"""
Nombre: Galilea Peralta Contreras.
Fecha: 02 de abril del 2025.

Descripción:
Se desea desarrollar un sistema en Python para gestionar un torneo de fútbol en el que participan varios equipos, y cada equipo está compuesto por jugadores. El sistema debe considerar lo siguiente:

2. Gestionar Equipos:
Cada equipo tiene un nombre, un ID único (generado automáticamente) y una lista de jugadores.
Los equipos pueden agregar o remover jugadores, ya sea individualmente o en grupos.
Los atributos de los equipos deben estar protegidos, y se debe controlar el acceso a ellos mediante métodos de acceso.
Cada equipo debe poder calcular el total de goles anotados por todos sus jugadores
"""

# Se importa la clase Jugador desde el módulo Jugador.py
from Jugador import Jugador

class Equipo:
    no_id = 0
    def __init__(self,nombre:str, *jugadores:tuple[Jugador]):
        """
        :param nombre: Nombre del equipo.
        :param jugadores: Lista de jugadores.
        """
        Equipo.no_id += 1  # Incrementa el contador de ID de equipos.
        self._nombre = nombre # Nombre del equipo
        self._jugadores = list(jugadores)  # Lista de jugadores del equipo.
        self._id_equipo = int(Equipo.no_id)  # Asigna el ID único al equipo.

    def agregar_jugadores(self, *jugadores:tuple[Jugador]) -> None:
        """
        Agrega jugadores al equipo si no están ya en él.
        :param jugadores: Lista de jugadores a agregar.
        """
        for jugador in jugadores:
            if jugador not in self._jugadores:
                self._jugadores.append(jugador)
            else:
                print(f"El jugador {jugador} forma parte del equipo {self.nombre}.")

    def eliminar_jugadores(self,  *jugadores:tuple[Jugador]) -> None:
        """
        Elimina jugadores del equipo si están en él.
        :param jugadores: Lista de jugadores a eliminar.
        """
        for jugador in jugadores:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)
            else:
                print(f"El jugador {jugador} no forma parte del equipo {self.nombre}.")

    def mostrar_jugadores(self) -> None:
        """
        Muestra la lista de jugadores del equipo.
        """
        print(f"*** Lista de jugadores del equipo de {self.nombre} ***")
        for jugador in self._jugadores:
            print(jugador)

    def total_goles(self) -> int:
        """
        Calcula el total de goles anotados por todos los jugadores del equipo.
        :return: Total de goles.
        """
        puntos = 0
        for jugador in self._jugadores:  #Suma los goles de cada jugador.
            puntos += jugador._goles
        return int(puntos)

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
        """
        Devuelve una representación en cadena del equipo.
        """
        # Se convierte los elementos de la lista en cadenas (invocando str() para cada uno de ellos) y
        # se unen con ", " a través del métod0 str.join().
        # Este patrón es muy común en Python para obtener una cadena a partir de una lista.
        jugadores = ", ".join(str(jugador) for jugador in self._jugadores)
        return f"Equipo (Nombre: {self._nombre},  id: {self._id_equipo}, jugadores = {jugadores} )"


def main() -> None:
    """
    Función principal.
    """

    # Crear jugadores
    jugador1 = Jugador("Carlos", 5,6)
    jugador2 = Jugador("Luis", 3,8)
    jugador3 = Jugador("Pedro", 7,3)

    # Crear equipo con algunos jugadores
    equipo = Equipo("Unsij", jugador1, jugador2)

    print(" Mostrar la información del equipo")
    print(equipo)

    print()
    print(" Agregar un nuevo jugador y mostrarlo")
    equipo.agregar_jugadores(jugador3)
    equipo.mostrar_jugadores()

    print()
    print(" Eliminar un nuevo jugador y mostrarlo")
    equipo.eliminar_jugadores(jugador1)
    equipo.mostrar_jugadores()

    print()
    print("Mostrar total de goles del equipo")
    print(f"Total de goles del equipo: {equipo.total_goles()}")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()