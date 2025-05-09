"""
Nombre: Galilea Peralta Contreras.
Fecha: 31 de marzo del 2025.

Descripción:

    1 devuelve "Sunday"
    2 devuelve "Monday"
    3 devuelve "Tuesday"
    4 devuelve "Wednesday"
    5 devuelve "Thursday"
    6 devuelve "Friday"
    7 devuelve "Saturday"
    De lo contrario devuel "Wrong, please enter a number between 1 and 7"
"""


def whatday(num:int) -> str:
    """
    Devuelve el nombre del día de la semana correspondiente a un número.
    :param num: Número entero entre 1 y 7.
    :return: Nombre del día de la semana o mensaje de error.
    """

    if num == 1:
        return "Sunday"
    elif num == 2:
        return "Monday"
    elif num == 3:
        return "Tuesday"
    elif num == 4:
        return "Wednesday"
    elif num == 5:
        return "Thursday"
    elif num == 6:
        return "Friday"
    elif num == 7:
        return "Saturday"
    else:
        return "Wrong, please enter a number between 1 and 7"


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
    num = input("Números de tostadas que tiene: ")
    num = cadena_a_entero(num)
    while num == None:
        num = input(f"Ingrese un número: ")
        num = cadena_a_entero(num)

    print(whatday(num))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()