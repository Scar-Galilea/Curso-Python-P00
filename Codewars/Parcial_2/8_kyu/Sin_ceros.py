"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:

"""

def no_boring_zeros(n: str)-> int:
    cont = 0
    n = str(n)
    for i in n:
        if i == '0':
            cont += 1
        else:
            cont = 0
    cont = cont * - 1
    if n == "0" or n == "":
        return 0
    elif n[-1] != "0":
        return int(n)
    else:
        return int(n[0:cont])

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(no_boring_zeros(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()