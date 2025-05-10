"""
Nombre: Galilea Peralta Contreras.
Fecha: 07 de abril del 2025.

Descripción:
Implementar la función que debe volver true si se da objeto es una vocal
(es decir, a, e, i, o, u, mayúscula o minúscula), y false de otra manera.
"""

def is_vowel(s:str)-> bool:
    """
    Verifica si el caracter corresponde a una vocal.
    :param s:
    :return: True si es un solo una vocal, False en cualquier otro caso.
    """
    s = s.lower()
    if s =='a' or s =='e' or s =='i'or s =='o'or s =='u':
        return True
    else:
        return False


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese un caracter: ") # Solicita la entrada del usuario.
    print(is_vowel(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
