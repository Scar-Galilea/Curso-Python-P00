"""
Nombre: Galilea Peralta Contreras.
Fecha: 07 de abril del 2025.

Descripción:


"""
#La función ord regresa el número ACCI
def is_letter(s:str)->bool:
    if len(s) == 1:
        n = ord(s)
        print(n)
        if 65 <= n <= 90 or 97 <= n <= 122:
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
    print(is_letter(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()