"""
Nombre: Galilea Peralta Contreras.
Fecha: 07 de abril del 2025.

Descripción:


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