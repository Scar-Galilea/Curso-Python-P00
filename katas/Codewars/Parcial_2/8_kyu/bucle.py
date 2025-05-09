"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Su collegue escribió un bucle simple para enumerar sus animales favoritos. Pero parece haber un pequeño error en la gramática, que impide que el programa funcione. Arréglalo. :)
Si pasas la lista de tus animales favoritos a la función, debes conseguir la lista de los animales con pedidos y nuevas líneas añadidas.

Por ejemplo, de paso:
[ "dog", "cat", "elephant" ]

dará como resultado:
"1. dog\n2. cat\n3. elephant\n"


"""

def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst




def main() -> None:
    """
    Función principal.
    """
    #Arregla para pedir una lista
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(list_animals(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()