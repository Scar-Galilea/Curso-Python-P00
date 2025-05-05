"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
La raíz digital es la suma recursiva de todos los dígitos en un número.

Dado n, tomar la suma de los dígitos de n. Si ese valor tiene más de un dígito, siga reduciéndose de esta manera hasta que se produzca un número de un solo dígito. La entrada será un entero no negativo.
Ejemplos

    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


"""

def digital_root(n:int)->int:
    suma = n
    while len(str(n)) != 1:
        suma = 0
        for i in str(n):
            suma += int(i)
        n = suma
    return suma


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(digital_root(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()