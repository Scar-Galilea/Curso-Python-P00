"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Escribe una función que tome un array de números y devuelva la suma de estos. Los números pueden ser negativos o no enteros. Si el array no contiene ningún número, debes devolver 0.

Ejemplos
Entrada: [1, 5.2, 4, 0, -1]
Salida:9.2

Entrada: []
Salida:0

Entrada: [-2.398]
Salida:-2.398

Suposiciones
Puedes asumir que solo te dan números.
No se puede asumir el tamaño de la matriz.
Puedes asumir que obtienes una matriz y si la matriz está vacía, devuelves 0.

Estamos probando bucles y operaciones matemáticas básicas. Esto es para principiantes que están aprendiendo bucles y operaciones matemáticas.
Los usuarios avanzados pueden encontrarlo extremadamente fácil y pueden escribirlo fácilmente en una sola línea.
"""

def sum_array(a):
    return sum(a)

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(sum_array(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()