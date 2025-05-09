"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Mientras hacía un juego, su pareja, Greg, decidió crear una función para comprobar si el usuario sigue vivo llamado checkAlive/CheckAlive/check_alive. Desafortunadamente, Greg cometió algunos errores al crear la función.
checkAliveCheckAlive// check_alivedebe devolverlo fiel si la salud del jugador es mayor que 0 o falsa si es 0 o inferior.
La función recibe un parámetro healthque siempre será un número entero entre -10 y 10.
"""

def check_alive(health: int)->bool:
    if health <= 0:
        return False
    else:
        return True

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(check_alive(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()