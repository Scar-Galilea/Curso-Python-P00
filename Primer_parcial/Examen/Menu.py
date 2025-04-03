"""
Nombre: Galilea Peralta Contreras.
Fecha: 02 de abril del 2025.

Descripción:
Se desea desarrollar un sistema en Python para gestionar un torneo de fútbol en el que participan varios equipos, y cada equipo está compuesto por jugadores. El sistema debe considerar lo siguiente:

1. Gestionar Jugadores:
Cada jugador tiene un nombre, un número y una cantidad de goles anotados.
Los jugadores pueden anotar goles, y el sistema debe actualizar su contador de goles.
Los atributos de los jugadores deben estar protegidos, y se debe controlar el acceso a ellos mediante métodos de acceso.

2. Gestionar Equipos:
Cada equipo tiene un nombre, un ID único (generado automáticamente) y una lista de jugadores.
Los equipos pueden agregar o remover jugadores, ya sea individualmente o en grupos.
Los atributos de los equipos deben estar protegidos, y se debe controlar el acceso a ellos mediante métodos de acceso.
Cada equipo debe poder calcular el total de goles anotados por todos sus jugadores.

3. Gestionar Torneos:
Cada torneo tiene un nombre y una lista de equipos participantes.
Los torneos pueden agregar o remover equipos, ya sea individualmente o en grupos.
El sistema debe permitir mostrar la lista de equipos participantes en el torneo.
El sistema debe generar un rol de partidos estilo "todos contra todos", organizado por jornadas de todos los equipos participantes, donde cada jornada contenga un conjunto de partidos que no se solapen (es decir, ningún equipo juegue más de un partido por jornada).

4. Relaciones entre Clases:
Un Equipo está compuesto por varios Jugadores (relación de agregación).
Un Torneo está compuesto por varios Equipos (relación de agregación).

5. Requerimientos técnicos:
Usar encapsulamiento para proteger los atributos de las clases.
Usar métodos de acceso (@property y @<atributo>.setter) para controlar el acceso a los atributos.
Implementar métodos para agregar y remover múltiples objetos (jugadores o equipos) usando argumentos variables (*args).
Implementar métodos para mostrar información de manera legible ( __str__() ).
Implementar un método para generar un rol de partidos estilo "todos contra todos" organizado por jornadas.
Implementar un método para calcular el total de goles de un equipo.

6. Diseño del módulo principal (Main.py):
Se requiere diseñar una interfaz en consola (menú) que permita:
Crear nuevos jugadores y equipos, solicitando los datos requeridos para cada objeto.
Ver lista de jugadores y equipos, mostrando la lista de todos los objetos.
Agregar jugadores a algún equipo. En este caso, se debe mostrar un submenú que indique los jugadores para seleccionar, luego otro submenú que indique a qué equipo se quiere añadir. Nota: No se considera el caso de que un jugador pertenezca a dos equipos.
Eliminar jugadores de un equipo. En este caso, se debe mostrar un submenú con la lista de equipos, después de seleccionar a alguno de ellos, se debe de mostrar la lista de jugadores a eliminar del equipo.
Agregar equipos al torneo. En este caso, se debe mostrar un submenú que indique los equipos a añadir al torneo. Nota: no se considera el caso de que un equipo se inscriba más de una vez.
Eliminar equipos del torneo. En este caso, se debe mostrar un submenú con la lista de equipos a remover del torneo.
Anotar gol(es) a un jugador. En este caso, se debe solicitar la cantidad de goles a anotar y que escoja a un jugador (mostrando la lista).
Conocer el número total de goles de los equipos. En este caso, se debe mostrar los goles totales de cada equipo.
Generar rol de juegos. Generar un rol de juegos con los equipos del torneo estilo "todos contra todos" organizado por jornadas.
Nota: Se considera que se tiene un único objeto de la clase Torneo.
"""

from Torneo import Torneo
from Equipo import Equipo
from Jugador import Jugador

def menu() -> int:
    print("***  Bienvenido al torneo: Champios League. ***")
    print("1) Crear nuevos jugadores.")
    print("2) Crear nuevo equipo.")
    print("3) Ver listas de jugadores.")
    print("4) Ver listas de equipos.")
    print("5) Agregar jugadores a algún equipo.")
    print("6) Agregar jugadores a algún equipo.")
    print("7) Agregar equipos al torneo.")
    print("8) Eliminar equipos del torneo.")
    print("9) Anotar goles a un jugador.")
    print("10) Conocer el número total de goles de los equipos.")
    print("11) Generar rol de juegos.")
    print("0) Salir.")

    print()
    opcion = input("Elije una opción: ")

    while not opcion.isnumeric():
        print("Opción invalida")
        print("___________________________________________________________________")
        print()
        opcion = input("Intenta nuevamente: ")
        print()
    return int(opcion)

def cadena_a_entero(cadena: str) -> int | None:
    """
    Muestra el menu del programa
    :param cadena: Lo que ingresa el usuario
    :return: Un número entero o None
    """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in(0,1) :
        return  int(cadena)
    else:
        return None

def main() -> None:
    opcion = None

    while opcion != 0:
        opcion = menu()
        if opcion == 0:
            print("Fin del programa.")
        elif opcion == 1:
            lista_jugadores = Equipo("Lista de jugadores")
            nombre_jugador = input("Ingrese el nombre del jugador: o presiona 2 enter para continuar: ")
            num_jugador = input("Ingrese el número del jugador  o presiona enter para continuar: ")

            while bool(num_jugador):
                # Se convierte la cadena ingresada a un número entero si es válido
                numero = cadena_a_entero(cadena=num_jugador)

                if numero is None:
                    print("Formato no válido, intenta nuevamente.")

                jugador_x = Jugador(nombre_jugador,num_jugador)
                lista_jugadores.agregar_jugadores(jugador_x)

                nombre_jugador = input("Ingrese el nombre del jugador o presiona 2 enter para continuar:")
                num_jugador = input("Ingrese el número del jugador  o presiona enter para continuar:")
        elif opcion == 2:
            lista_equipos = Torneo("Lista de equipos")
            nombre_equipo = input("Ingrese el nombre del equipor: o presiona  enter para continuar: ")

            while bool(nombre_equipo):
                equipo_x = Equipo(nombre_equipo)
                lista_equipos.agregar_equipos(equipo_x)
                nombre_equipo = input("Ingrese el nombre del equipor: o presiona  enter para continuar: ")

        elif opcion == 3:
            lista_jugadores.mostrar_jugadores()
            print()
        elif opcion == 4:
            lista_equipos.mostrar_equipos()
            print()
        elif opcion == 5:
            print()
        elif opcion == 6:
            print()
        elif opcion == 7:
            print()
        elif opcion == 8:
            print()
        elif opcion == 9:
            print()
        elif opcion == 10:
            print()
        elif opcion == 11:
            print()
        else:
            print("Opción invalida")
        print()

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()