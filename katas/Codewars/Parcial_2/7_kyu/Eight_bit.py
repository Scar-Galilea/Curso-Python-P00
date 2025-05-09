"""
Nombre: Galilea Peralta Contreras.
Fecha: 07 de abril del 2025.

Descripción:
Implementar String#eight_bit_number?, que debe devolverse true si se da objeto es un número que representa por 8 bits entero sin firmar (0-255), falsede otra manera.
Sólo debería aceptar números en representación canónica, así que no liderar +, extra 0s, espacios, etc.



"""
def eight_bit_number(n:str) -> bool:

    if n.isnumeric():
        n1 = n
        n = int(n)
        if len(n1) >= 2 and n1[0] == '0':
            return False
        if 255 >= n >= 0:
            return True
        else:
            return False
    else:
        return False


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(eight_bit_number(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()