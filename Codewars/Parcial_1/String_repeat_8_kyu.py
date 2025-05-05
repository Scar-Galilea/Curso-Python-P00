"""
Nombre: Galilea Peralta Contreras.
Fecha: 31 de marzo del 2025.

Descripción:
Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.
Examples (input -> output)

6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"

"""

def repeat_str(repeat: int, string: str) -> str:
    """
    Repite la cadena 'string' 'repeat' veces.
    :param repeat: Número de veces que se repetirá la cadena.
    :param string: La cadena a repetir.
    :return: La cadena repetida el número de veces indicado.
    """

    return string * repeat

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

    repeat = (input("Ingrese el parametro: "))
    repeat = cadena_a_entero(repeat)

    while repeat is None:
        repeat = input(f"Vuelve intentarlo los parametros: ")
        repeat = cadena_a_entero(repeat)

    string = input("Ingrese la cadena: ")

    print(repeat_str(repeat,string))


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()