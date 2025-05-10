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

def sum_array(a: list[int]) -> int:
    """
    Calcula la suma de cada elemento que contiene la lista.
    :param a: Lista de números.
    :return: Suma de los elementos de s.
    """
    return sum(a)

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
    suma = []
    num_cadena = input(f"Ingresa un número  o presiona enter para continuar: ")

    while bool(num_cadena):
        # Se convierte la cadena ingresada a un número entero si es válido
        numero = cadena_a_entero(cadena=num_cadena)

        if numero is None:
            print("Formato no válido, intenta nuevamente.")
        # Si el número es impar, se ignora y no se suma.
        else:
            suma.append(numero)

        num_cadena = input(f"Ingresa un  número o presiona enter para continuar: ")
    print(sum_array(suma))
""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()