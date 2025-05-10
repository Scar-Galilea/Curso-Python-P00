"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Oh no, Timmy ha creado un bucle infinito. Ayuda a Timmy a encontrar y arreglar el insecto en su inacabado para bucle.

"""

def create_array(n:int)->list[int]:
    """
    Crea una lista con los números enteros del 1 hasta n.
    :param n: Número entero positivo que indica el final de la secuencia.
    :return: Lista de números desde 1 hasta n.
    """
    lista = []
    for i in range(1,n+1):
        lista.append(i)
    return lista

def cadena_a_entero(cadena: str) -> int | None:
    """
    Muestra el menu del programa.
    :param cadena: Lo que ingresa el usuario.
    :return: Un número entero o None.
    """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in(0,1) :
        return  int(cadena)
    else:
        return None

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese número: ") # Solicita la entrada del usuario.
    n = cadena_a_entero(n)

    while n is None:
        n = input(f"Vuelve intentarlo: ")
        n = cadena_a_entero(n)
    print(create_array(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()