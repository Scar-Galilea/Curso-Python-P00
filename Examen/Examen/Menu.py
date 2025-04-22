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
    """
    Muestra el menú principal del programa.
    :return opción seleccionada por el usuario.
    """
    print("***  Bienvenido al torneo: Champios League. ***")
    print("1) Crear nuevos jugadores.")
    print("2) Crear nuevo equipo.")
    print("3) Ver listas de jugadores.")
    print("4) Ver listas de equipos.")
    print("5) Agregar jugadores a algún equipo.")
    print("6) Eliminar jugadores a algún equipo.")
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
    """
    Convierte una cadena en entero positivo.
    :return Número positivo o None si no es un número válido.
    """
    if cadena.isnumeric():
        return  int(cadena)
    else:
        return None

def main() -> None:
    opcion = None
    lista_jugadores = []  # Lista de jugadores creados.
    lista_equipos = [] # Lista global de equipos creados.
    torneo_principal = Torneo("Champios League") # Único torneo creado.

    while opcion != 0:
        opcion = menu()
        if opcion == 0:
            print("Fin del programa.")
        elif opcion == 1:
            # Crear jugadores.
            nombre_jugador = input("Ingrese el nombre del jugador: o presiona 2 enter para terminar: ")
            num_jugador = input("Ingrese el número del jugador o presiona enter para terminar: ")

            while bool(num_jugador) and bool(nombre_jugador):
                num_jugador = cadena_a_entero_positivo(num_jugador)
                while num_jugador is None:
                    num_jugador  = input(f"Ingrese nuevamente el numero del jugador: ")
                    num_jugador = cadena_a_entero_positivo(num_jugador)


                lista_jugadores.append(Jugador(nombre_jugador,num_jugador))
                print()

                nombre_jugador = input("Ingrese el nombre del jugador o presiona 2 enter para terminar: ")
                num_jugador = input("Ingrese el número del jugador  o presiona enter para terminar: ")


        elif opcion == 2:
            # Crear equipos.
            nombre_equipo = input("Ingrese el nombre del equipor: o presiona  enter para continuar: ")

            while bool(nombre_equipo):
                lista_equipos.append(Equipo(nombre_equipo))
                nombre_equipo = input("Ingrese el nombre del equipor: o presiona  enter para continuar: ")

        elif opcion == 3:
            # Mostrar jugadores.
            for i in lista_jugadores:
                print(i.nombre)


        elif opcion == 4:
            # Mostrar equipos
            for i in lista_equipos:
                print(i.nombre)

        elif opcion == 5:
            # Agregar jugadores a equipos.
            if len(lista_jugadores)> 0 and len(lista_equipos) > 0:
                for i in lista_jugadores:
                    print(i.nombre)
                nombre_agregar = input("Ingrese el nombre del jugador que desea agregar: ")
                print()

                for i in lista_equipos:
                    print(i.nombre)
                nombre_equipo = input("Ingrese el nombre del equipo donde iria el jugador: ")

                while bool(nombre_agregar) and bool(nombre_equipo):

                    for equipo in lista_equipos:
                        if nombre_equipo == equipo.nombre:
                            for j in lista_jugadores:
                                if nombre_agregar == j.nombre:
                                    equipo.agregar_jugadores(j)
                                    print("Se agrego con exito. ")

                    print()
                    for i in lista_jugadores:
                        print(i.nombre)
                    nombre_agregar = input("Ingrese el nombre del jugador que desea agregar: ")
                    print()

                    for i in lista_equipos:
                        print(i.nombre)
                    nombre_equipo = input("Ingrese el nombre del equipo donde iria el jugador: ")
            else:
                print("No se han creado equipo o jugadores.")

        elif opcion == 6:
            # Eliminar jugadores de equipos.
            if len(lista_jugadores) > 0 and len(lista_equipos) > 0:
                for i in lista_jugadores:
                    print(i.nombre)
                nombre_eliminar = input("Ingrese el nombre del jugador que desea eliminar: ")
                print()

                for i in lista_equipos:
                    print(i)
                nombre_equipo = input("Ingrese el nombre del equipo donde esta el jugador : ")

                while bool(nombre_eliminar) and bool(nombre_equipo):

                    for equipo in lista_equipos:
                        if nombre_equipo == equipo.nombre:
                            for j in lista_jugadores:
                                if nombre_eliminar == j.nombre:
                                    equipo.agregar_jugadores(j)
                                    print("Se elimino con exito.")

                    print()
                    for i in lista_jugadores:
                        print(i.nombre)
                    nombre_eliminar = input("Ingrese el nombre del jugador que desea eliminar: ")
                    print()

                    for i in lista_equipos:
                        print(i)
                    nombre_equipo = input("Ingrese el nombre del equipo donde esta el jugador: ")
            else:
                print("No se han creado equipo o jugadores.")

        elif opcion == 7:
            # Agregar equipos al torneo.
            if len(lista_equipos) > 0:

                for i in lista_equipos:
                    print(i.nombre)
                nombre_equipo = input("Ingrese el nombre del equipo que desea agregar del torneo o enter para salir: ")

                while bool(nombre_equipo):
                    for equipo in lista_equipos:
                        if equipo.nombre == nombre_equipo:
                            torneo_principal.agregar_equipos(equipo)
                            print("Se agrego correctamente.")

                    nombre_equipo = input("Ingrese el nombre del equipo que desea agregar torneo o enter para salir: ")
            else:
                print("No se han creado equipos.")

        elif opcion == 8:
            # Eliminar equipos del torneo.
            if len(torneo_principal.equipos) > 0:
                torneo_principal.mostrar_equipos()
                nombre_equipo = input("Ingrese el nombre del equipo que desea eliminar del torneo o enter para salir: ")

                while bool(nombre_equipo):
                    for equipo in torneo_principal.equipos:
                        if equipo.nombre == nombre_equipo:
                            torneo_principal.eliminar_equipos(equipo)
                            print("Se elimino correctamente.")


                    nombre_equipo = input( "Ingrese el nombre del equipo que desea eliminar torneo o enter para salir: ")
            else:
                print("No se hay equipos del torneo que eliminar.")
        elif opcion == 9:
            # Anotar goles a jugador.
            if len(lista_equipos) > 0:
                for i in lista_jugadores:
                    print(i.nombre)
                b = 0
                nombre_jugador = input("Ingrese el nombre del jugador que anotó gol: ")
                gol = input("Ingresa la cantidad de goles: ")
                gol =cadena_a_entero_positivo(gol)
                while gol is None:
                    gol  = input(f"Ingrese nuevamente el gol del jugador: ")
                    gol = cadena_a_entero_positivo(gol)

                for equipo in lista_equipos:
                        for j in equipo.jugadores:
                            if j.nombre == nombre_jugador:
                                j.anotar_goles(gol)
                                b = 1
                if b == 0:
                    print("El jugador no pertenece a un equipo.")
            else:
                print("No se ha formado ningun equipo para que el jugador meta gol.")
        elif opcion == 10:
            # Total de goles por equipo.
            for i in lista_equipos:
                print(i.nombre)
            nombre_equipo = input("Seleccione el equipo que desea conocer el número total de goles: ")
            if len(lista_equipos) > 0:
                for equipo in lista_equipos:
                    if equipo.nombre == nombre_equipo:
                        print(equipo.nombre)
                        print(equipo.total_goles())
                        print()
            else:
                print("No hay un equipo.")
        elif opcion == 11:
            # Generar rol de juegos (jornadas)
            if len(torneo_principal.equipos) > 0:
                torneo_principal.generar_rol()
            else:
                print("No hay equipos en el torneo.")
        else:
            print("Opción invalida.")
        print()

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()