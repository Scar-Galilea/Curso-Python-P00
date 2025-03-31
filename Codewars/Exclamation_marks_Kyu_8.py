"""
Nombre: Galilea Peralta Contreras.
Fecha: 31 de marzo del 2025.

Descripción:

"""


def six_toast(num: int) -> int:

    num = num-6
    # abs es una función de valor absoluto
    num = abs(num)
    return num


def cadena_entero(cadena: str) -> int | None:
    """
    Convertir una cadena a flotante.
    :return: Un número cadena o none.
    """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".", "")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None


def main() -> None:
    """
    Función principal.
    """

    num = input("Números de tostadas que tiene: ")

    print(six_toast(num))

    while  num  == None:
        num = input(f"Vuelve intentarlo: ")
        num = cadena_entero(num)



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()