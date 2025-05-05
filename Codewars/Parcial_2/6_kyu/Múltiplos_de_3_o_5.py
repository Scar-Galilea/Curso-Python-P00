"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Si enumeramos todos los números naturales por debajo de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.

Terminar la solución para que devuelva la suma de todos los múltiplos de 3 o 5 por debajo del número pasado.

Además, si el número es negativo, devuelva 0.

Nota: Si el número es un múltiplo de both3 y 5, sólo cuenta una vez.

Cortesía de projecteuler.net (Problem 1)

"""

def solution(number:int):
    num = 0
    if number >= 4:
        for i in range(3,number):
            if i % 3 == 0 or i % 5 == 0:
                num += i
    return num


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(solution(int(n)))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()