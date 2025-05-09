"""
Nombre: Galilea Peralta Contreras.
Fecha: 07 de abril del 2025.

Descripción:
¿Implementar String#six_bit_number?, que debe devolver la verdad si se da objeto es un número representable por 6 bits sin firmar entero (0-63), false de otra manera.
Solo debería aceptar números en representación canónica, así que no liderar +, extra 0s, espacios, etc.
"""
def six_bit_number(n:str)-> bool:
    if n.isnumeric():
        n1 = n
        n=int(n)
        if len(n1) >= 2 and n1[0] == '0':
            return False
        if 63 >= n >= 0 :
            return True
        else:
            return False
    else:
        return False


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese una frase: ") # Solicita la entrada del usuario.
    print(six_bit_number(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()