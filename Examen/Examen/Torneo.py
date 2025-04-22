"""
Nombre: Galilea Peralta Contreras.
Fecha: 02 de abril del 2025.

Descripción:
Se desea desarrollar un sistema en Python para gestionar un torneo de fútbol en el que participan varios equipos, y cada equipo está compuesto por jugadores. El sistema debe considerar lo siguiente:

Gestionar Torneos:
Cada torneo tiene un nombre y una lista de equipos participantes.
Los torneos pueden agregar o remover equipos, ya sea individualmente o en grupos.
El sistema debe permitir mostrar la lista de equipos participantes en el torneo.
El sistema debe generar un rol de partidos estilo "todos contra todos", organizado por jornadas de todos los equipos participantes, donde cada jornada contenga un conjunto de partidos que no se solapen (es decir, ningún equipo juegue más de un partido por jornada).
"""

from Equipo import Equipo
from Jugador import Jugador

class Torneo:
    def __init__(self,nombre:str, *equipos:Equipo):
        """
        Constructor de la clase Torneo.
        :param nombre: Nombre del torneo.
        :param equipos: Equipos que participarán en el torneo.
        """
        self._nombre = nombre
        self._equipos = list(equipos)

    def agregar_equipos(self,*equipos:Equipo) -> None:
        """
        Agrega uno o más equipos al torneo si no están ya registrados.
        :param equipos: Lista de equipos a agregar.
        """
        for equipo in equipos:
            if equipo not in self._equipos:
                self._equipos.append(equipo)
            else:
                print(f"El equipo {equipo} forma parte del equipo {self.nombre}.")

    def eliminar_equipos(self, *equipos: Equipo) -> None:
        """
        Elimina uno o más equipos del torneo si están registrados.
        :param equipos: Lista de equipos a eliminar.
        """
        for equipo in equipos:
            if equipo in self._equipos:
                self._equipos.remove(equipo)
            else:
                print(f"El equipo {equipo} no forma parte del equipo {self.nombre}.")

    def mostrar_equipos(self) -> None:
        """
        Muestra la lista de equipos participantes en el torneo.
        """
        print(f"*** Lista de jugadores del equipo de {self.nombre} ***")
        for equipo in self._equipos:
            print(equipo)

    def generar_rol(self) -> None:
        """
        Genera un rol de partidos estilo "todos contra todos", distribuidos en jornadas.
        """
        numero_de_equipos = len(self._equipos)
        equipos = list(self._equipos)  # Copia para no modificar la original

        if numero_de_equipos % 2 != 0:
            auxiliar = Torneo("Auxiliar")
            equipos.append(auxiliar)
            numero_de_equipos = numero_de_equipos + 1

        se = int(numero_de_equipos / 2)  # Número de partidos por jornada
        grupo = 0


        while grupo < numero_de_equipos - 1:  # Se genera el número correcto de jornadas
            contador = 0
            print(f"Jornada {grupo + 1}:")

            # Mostrar los enfrentamientos del grupo actual.

            while contador < se:
                print(equipos[contador].nombre, end=" vs ")
                print(equipos[numero_de_equipos - 1 - contador].nombre)
                contador += 1

            # Rotación de equipos, dejando fijo el primero
            equipos.insert(1, equipos.pop())
            grupo += 1
            print()


    # Métodos de acceso para obtener atributos encapsulados.
    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def equipos(self) -> list[Equipo]:
        return self._equipos

    # Métodos modificadores (setter) para cambiar valores de los atributos encapsulados.
    @nombre.setter
    def nombre(self, nombre : str) -> None:
        self._nombre = nombre

    @equipos.setter
    def equipos(self, *equipos:Equipo) -> None:
        self._equipos = equipos

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del torneo.
        """
        # Se convierte los elementos de la lista en cadenas (invocando str() para cada uno de ellos) y
        # se unen con ", " a través del métod0 str.join().
        # Este patrón es muy común en Python para obtener una cadena a partir de una lista.
        equipos = ", ".join(str(equipo) for equipo in self._equipos)
        return f"Torneo (Nombre: {self._nombre},  equipos: ({equipos})"


def main() -> None:
    """
    Función principal.
    """
    # Crear equipos\
    jugador1 = Jugador("Carlos", 5, 6)
    jugador2 = Jugador("Luis", 3, 8)
    jugador3 = Jugador("Pedro", 7, 3)
    jugador4 = Jugador("Alberto", 8, 2)
    jugador4 = Jugador("ana", 8, 2)

    equipo1 = Equipo("Leones",jugador1)
    equipo2 = Equipo("Tiburones",jugador2)
    equipo3 = Equipo("Águilas",jugador3)
    equipo4 = Equipo("Dragones", jugador4)

    # Crear torneo y agregar equipos
    torneo = Torneo("Copa Unsij", equipo1, equipo2)

    # Mostrar información del torneo
    print("Mostrar información del torneo")
    print(torneo)
    torneo.mostrar_equipos()

    print()
    print("Agregar más equipos y mostrar")
    torneo.agregar_equipos(equipo3, equipo4)
    torneo.mostrar_equipos()

    print()
    # Generar el rol de partidos
    torneo.generar_rol()


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()