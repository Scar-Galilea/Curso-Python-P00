"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
La raíz digital es la suma recursiva de todos los dígitos en un número.

Dado n, tomar la suma de los dígitos de n. Si ese valor tiene más de un dígito, siga reduciéndose de esta manera hasta que se produzca un número de un solo dígito. La entrada será un entero no negativo.
Ejemplos

    16 --> 1 + 6 = 7
   942 --> 9 + 4 + 2 = 15 --> 1 + 5 = 6
132189 --> 1 + 3 + 2 + 1 + 8 + 9 = 24 --> 2 + 4 = 6
493193 --> 4 + 9 + 3 + 1 + 9 + 3 = 29 --> 2 + 9 = 11 --> 1 + 1 = 2


"""

def digital_root(n:int)->int:
    """
    Calcula la raíz digital de un número entero positivo.
    :param n: Número entero del cual se quiere obtener la raíz digital.
    :return: La raíz digital como un número de un solo dígito.
    """
    suma = n # Inicialmente, la suma es el número original.

    while len(str(n)) != 1: # Mientras el número tenga más de un dígito (longitud mayor que 1).
        suma = 0  # Reinicia la suma.
        # Se recorre cada dígito del número convirtiéndolo a cadena.
        for i in str(n):
            suma += int(i) # Se convierte cada carácter en número y se suma
        n = suma
    return suma

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
    n = input("Ingrese un número: ") # Solicita la entrada del usuario.
    n = cadena_a_entero(n)

    while  n  is None:
        n = input(f"Vuelve intentarlo: ")
        n= cadena_a_entero(n)

    print(digital_root(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()