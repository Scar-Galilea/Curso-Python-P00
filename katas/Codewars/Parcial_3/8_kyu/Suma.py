"""
Nombre: Galilea Peralta Contreras.
Fecha: 20 de mayo del 2025.

Descripción:
You get an array of numbers, return the sum of all of the positives ones.
Example

    [1, -4, 7, 12] => 1+7+12=20 1 + 7 + 12 = 20 1+7+12=20

Note

If there is nothing to sum, the sum is default to 0.
"""

def positive_sum(arr):
    suma = sum(arr)
    for i in arr:
        if str(i)[0] == "-":
            suma = suma - i
    return suma


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(positive_sum(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()