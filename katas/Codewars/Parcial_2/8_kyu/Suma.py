"""
Nombre: Galilea Peralta Contreras.
Fecha: 07 de abril del 2025.

Descripción:
¿Implementar String#six_bit_number?, que debe devolver la verdad si se da objeto es un número representable por 6 bits sin firmar entero (0-63), false de otra manera.
Solo debería aceptar números en representación canónica, así que no liderar +, extra 0s, espacios, etc.
"""

def sum_str(a, b):
    if (a is not None and a.isnumeric()) and (b is not None and b.isnumeric()):
        a = int(a)
        b = int(b)
        return str(a+b)
    elif a == "" and b.isnumeric():
        return b
    elif b == "" and a.isnumeric():
        return a
    else:
        return "0"




def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese una frase: ") # Solicita la entrada del usuario.
    n1 = input("Ingrese una frase: ")  # Solicita la entrada del usuario.
    print(sum_str(n,n1))




""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()