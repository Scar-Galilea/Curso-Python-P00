"""
Nombre: Galilea Peralta Contreras.
Fecha: 07 de abril del 2025.

Descripción:
¿Implementar String#six_bit_number?, que debe devolver la verdad si se da objeto es un número representable por 6 bits sin firmar entero (0-63), false de otra manera.
Solo debería aceptar números en representación canónica, así que no liderar +, extra 0 s, espacios, etc.
"""

def sum_str(a:str, b:str) -> str:
    """
    Suma dos valores enteros y retorna el resultado como cadena.

    :param a: Primer número entero.
    :param b: Segundo número entero.
    :return: Resultado como cadena si alguna entrada es inválida.
    """
    if (a is not None and a.isnumeric()) and (b is not None and b.isnumeric()):
        a = int(a)
        b = int(b)
        return str(a + b)
    elif a == "" and b.isnumeric():
        return b
    elif b == "" and a.isnumeric():
        return a
    else:
        return "0"


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
    n = input("Ingrese el  número para a: ")  # Solicita la entrada del usuario.
    n1 = input("Ingrese el  número para b: ")  # Solicita la entrada del usuario.

    print(sum_str(n,n1))




""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()