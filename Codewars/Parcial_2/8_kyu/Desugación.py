"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Mientras hacía un juego, su pareja, Greg, decidió crear una función para comprobar si el usuario sigue vivo llamado checkAlive/CheckAlive/check_alive. Desafortunadamente, Greg cometió algunos errores al crear la función.
checkAliveCheckAlive// check_AlivePDF devolverlo fiel si la salud del jugador es mayor que 0 o falsa si es 0 o inferior.
La función recibe un parámetro health siempre será un número entero entre -10 y 10.
"""

def check_alive(health: int) -> bool:
    """
    Verifica si el jugador sigue con vida.
    :param health: Valor entero de la salud del jugador.
    :return: True si la salud es mayor que 0, False en caso contrario.
    """
    if health <= 0:
        return False
    else:
        return True

def cadena_a_entero(cadena: str) -> int | None:
    """
    Muestra el menu del programa.
    :param cadena: Lo que ingresa el usuario.
    :return: Un número entero o None.
    """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in(0,1) :
        return  int(cadena)
    else:
        return None

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    n = cadena_a_entero(n)

    while n is None:
        n = input(f"Vuelve intentarlo: ")
        n = cadena_a_entero(n)

    print(check_alive(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()