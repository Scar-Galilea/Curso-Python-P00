"""
Nombre: Galilea Peralta Contreras.
Fecha: 31 de marzo del 2025.

Descripción:
You forgot to count the number of toast you put into there, you don't know if you put exactly six pieces of toast into the toasters.
Define a function that counts how many more (or less) pieces of toast you need in the toasters. Even though you need more or less, the number will still be positive, not negative.
Examples:
You must return the number of toast the you need to put in (or to take out). In case of 5 you can still put 1 toast in:
5 --> 1
And in case of 12 you need 6 toasts less (but not -6):
12 --> 6
"""


def six_toast(num: int) -> int:

    num = num-6
    # abs es una función de valor absoluto
    num = abs(num)
    return num


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
    """
    Función principal.
    """

    num = input("Números de tostadas que tiene: ")
    num = cadena_a_entero(num)
    while  num  is None:
        num = input(f"Vuelve intentarlo: ")
        num = cadena_a_entero(num)

    print(six_toast(num))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()