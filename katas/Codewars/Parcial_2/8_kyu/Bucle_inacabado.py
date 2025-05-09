"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Oh no, Timmy ha creado un bucle infinito. Ayuda a Timmy a encontrar y arreglar el insecto en su inacabado para bucle.

"""

def create_array(n:int)->list[int]:
    lista = []
    for i in range(1,n+1):
        lista.append(i)
    return lista

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(create_array(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()