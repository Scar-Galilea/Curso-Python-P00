"""
Nombre: Galilea Peralta Contreras.
Fecha: 10 de abril del 2025.

Descripción:
Necesita que crees un método que pueda determinar cuántos letters(mino mayúsculas y minúsculas ASCII) y digits están en una cuerda dada.

Ejemplo:

"hel2!lo" --> 6

"wicked .. !" --> 6

"!?..A" --> 1
"""
def count_letters_and_digits(s: str) -> int:
    """
    Cuenta cuántos caracteres de la cadena son letras (A-Z, a-z) o dígitos (0-9).
    :param s: Cadena de entrada que puede contener cualquier tipo de caracteres.
    :return: Número total de letras y dígitos en la cadena.
    """
    cont = 0 # Inicializa el contador.
    for i in s:
        # Verifica si el carácter es una letra mayúscula (A-Z), minúscula (a-z) o dígito (0-9).
        # La función ord() devuelve el valor numérico (código ASCII) de un carácter.
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
            cont += 1
    return cont

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese una palabra o oración: ") # Solicita la entrada del usuario.
    print(count_letters_and_digits(n))


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()