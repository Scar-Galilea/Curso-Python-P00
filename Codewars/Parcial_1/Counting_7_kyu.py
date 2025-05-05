"""
Nombre: Galilea Peralta Contreras.
Fecha: 31 de marzo del 2025.

Descripción:
The Arara is an isolated tribe found in the Amazon who count in pairs. For example one to eight is as follows:

1 = anane
2 = adak
3 = adak anane
4 = adak adak
5 = adak adak anane
6 = adak adak adak
7 = adak adak adak anane
8 = adak adak adak adak
Take a given number and return the Arara's equivalent.

e.g.

3 --> "adak anane"

8 --> "adak adak adak adak"

"""


def count_arara(n:int) -> str | None:
    """
    Convierte un número entero en su equivalente en el sistema de conteo Arara.
    :param n: Número a convertir.
    :return: Cadena con la representación en el sistema Arara.
    """
    n1 = int(n/2)
    if n%2 == 0:
        return "adak " * (n1-1) + "adak" # Retorna solo "adak" repetido si es par
    elif n%2 != 0:
        return "adak " *(n1) + "anane"

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

    n = input("Ingrese el número de parejas de la tribu Arara: ")
    n = cadena_a_entero(n)
    while n is None:
        n = input(f"Vuelve intentarlo: ")
        n = cadena_a_entero(n)

    print(count_arara(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()