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
def count_letters_and_digits(s):
    cont = 0
    for i in s:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
            cont += 1
    return cont

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese una frase: ") # Solicita la entrada del usuario.
    print(count_letters_and_digits(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()