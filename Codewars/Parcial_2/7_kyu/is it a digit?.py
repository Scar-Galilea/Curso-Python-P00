"""
Nombre: Galilea Peralta Contreras.
Fecha: 07 de abril del 2025.

Descripción:
Implementar String#digit?(en Java StringUtils.isDigit(String)),
que debería regresar truesi el objeto dado es un solo dígito (0-9), falsede otra manera.


"""
def is_digit(n:str) -> bool:

    if n.isnumeric():
        n1 = n
        n = int(n)
        if len(n1) >= 2 and n1[0] == '0':
            return False
        if 9 >= n >= 0:
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
    print(is_digit(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()