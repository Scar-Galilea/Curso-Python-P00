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
    print("6) eliminar jugadores a algún equipo.")
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

def cadena_a_entero_positivo(cadena: str) -> int | None:
    if cadena.isnumeric():
        return  int(cadena)
    else:
        return None

def main() -> None:
    opcion = None
    lista_jugadores = []
    lista_equipos = []
    x = Equipo("")
    y = Torneo("")
    torneo_principal = Torneo("Champios League")

    while opcion != 0:
        opcion = menu()
        if opcion == 0:
            print("Fin del programa.")
        elif opcion == 1:
            nombre_jugador = input("Ingrese el nombre del jugador: o presiona 3 enter para terminar: ")
            num_jugador = input("Ingrese el número del jugador o 2 presiona enter para terminar: ")
            num_goles = input("Ingrese el número del jugador o presiona enter para continuar: ")
            while bool(num_jugador) and bool(nombre_jugador) and bool(num_goles):
                jugador_x = []
                # Se convierte la cadena ingresada a un número entero si es válido
                num_jugador = cadena_a_entero_positivo(num_jugador)
                num_goles = cadena_a_entero_positivo(num_goles)
                while num_jugador is None:
                    num_jugador  = input(f"Ingrese nuevamente el numero del jugador: ")
                    num_jugador = cadena_a_entero_positivo(num_jugador)
                while num_goles is None:
                    num_goles  = input(f"Ingrese nuevamente el numero de goles: ")
                    num_goles = cadena_a_entero_positivo(num_goles)
                lista_jugadores.append(Jugador(nombre_jugador,num_jugador,num_goles))
                x.agregar_jugadores(Jugador(nombre_jugador,num_jugador,num_goles))
                print()

                nombre_jugador = input("Ingrese el nombre del jugador o presiona 3 enter para terminar:")
                num_jugador = input("Ingrese el número del jugador  o presiona 2 enter para terminar:")
                num_goles = input("Ingrese el número del jugador  o presiona enter para terminar: ")

        elif opcion == 2:
            nombre_equipo = input("Ingrese el nombre del equipor: o presiona  enter para continuar: ")

            while bool(nombre_equipo):
                lista_equipos.append(Equipo(nombre_equipo))
                y.agregar_equipos((Equipo(nombre_equipo)))
                nombre_equipo = input("Ingrese el nombre del equipor: o presiona  enter para continuar: ")

        elif opcion == 3:
            x.mostrar_jugadores()

        elif opcion == 4:
            y.mostrar_equipos()

        elif opcion == 5:
            if len(lista_jugadores)> 0 and len(lista_equipos) > 0:
                x.mostrar_jugadores()
                agregar_j = input("Ingrese el nombre del jugador que desea agregar")
                print()
                y.mostrar_equipos()
                agregar_e = input("Ingrese el nombre del equipo donde iria el jugador")

                for equipo in lista_equipos:
                    if equipo.nombre in agregar_e:
                        for jugadores in lista_jugadores:
                            if jugadores.nombre in  agregar_j:
                                equipo.agregar_jugadores(jugadores)
                        break
            else:
                print("No se han creado equipo o jugadores")

        elif opcion == 6:
            if len(lista_jugadores) > 0 and len(lista_equipos) > 0:
                agregar_j = input("Ingrese el nombre del jugador que desea agregar o enter para terminar: ")
                print()
                y.mostrar_equipos()
                agregar_e = input("Ingrese el nombre del equipo donde iria el jugador o enter para terminar: ")
                while bool(agregar_j) and bool(agregar_e) :
                    x.mostrar_jugadores()
                    for equipo in lista_equipos:
                        if equipo.nombre in agregar_e:
                            for jugadores in lista_jugadores:
                                    equipo.agregar_jugadores(jugadores)
                            break
                    print()
                    agregar_j = input("Ingrese el nombre del jugador que desea agregar o enter para terminar: ")
                    print()
                    y.mostrar_equipos()
                    agregar_e = input("Ingrese el nombre del equipo donde iria el jugador o enter para terminar: ")
            else:
                print("No se han creado equipo o jugadores")

        elif opcion == 7:
            if len(lista_equipos) > 0:
                y.mostrar_equipos()
                equipo_nombre = input("Ingrese el nombre del equipo a agregar al torneo: ")
                while bool(equipo_nombre):
                    for equipo in lista_equipos:
                        torneo_principal.agregar_equipos(equipo)
                    print()
                    equipo_nombre = input("Ingrese otro equipo o presione enter para finalizar: ")
            else:
                print("No se han creado equipos")


        elif opcion == 8:
            if len(lista_equipos) > 0:
                y.mostrar_equipos()
                equipo_nombre = input("Ingrese el nombre del equipo a eliminar del torneo: ")
                while bool(equipo_nombre):
                    torneo_principal.eliminar_equipos(equipo_nombre)
                    equipo_nombre = input("Ingrese otro equipo o presione enter para finalizar: ")
            else:
                print("No se han creado equipos")
        elif opcion == 9:
            if len(lista_jugadores) > 0:
                x.mostrar_jugadores()
                jugador_nombre = input("Ingrese el nombre del jugador que anotó: ")
                goles = input("Ingrese la cantidad de goles: ")
                goles = cadena_a_entero_positivo( goles)
                while  goles is None:
                    goles = input(f"Ingrese nuevamente los: ")
                    goles = cadena_a_entero_positivo(goles)

                for jugador in lista_jugadores:
                    if jugador.nombre == jugador_nombre:
                        jugador.anotar_goles(int(goles))
            else:
                print("No se han creado equipos")

        elif opcion == 10:
            for equipo in lista_equipos:
                print(equipo.nombre)
                equipo.total_goles()
                print()
        elif opcion == 11:
            if len(torneo_principal) > 0:
                torneo_principal.generar_rol()
                print()
            else:
                print("No hay equipos en el torneo")
        else:
            print("Opción invalida")
        print()

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()