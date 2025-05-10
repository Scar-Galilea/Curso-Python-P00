"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Su colleague escribió un bucle simple para enumerar sus animales favoritos. Pero parece haber un pequeño error en la gramática, que impide que el programa funcione. Arréglalo. :)
Si pasas la lista de tus animales favoritos a la función, debes conseguir la lista de los animales con pedidos y nuevas líneas añadidas.

Por ejemplo, de paso:
["dog", "cat", "elephant"]

Dará como resultado:
"1. Dog\n2. Cat\n3. Elephant\n"

"""

def list_animals(animals:list[str])-> str:
    """
    Genera una lista enumerada con los nombres de los animales capitalizados.
    :param animals: Lista de nombres de animales.
    :return: Cadena con cada animal enumerado y separado por saltos de línea.
    """
    lst = ''
    for i in range(len(animals)-1): # Se recorre toda la lista, que da el índice y el valor directamente.
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst

def main() -> None:
    """
    Función principal.
    """
    #Arregla para pedir una lista
    n = input("Ingrese un animal o presiona enter para continuar: ") # Solicita la entrada del usuario.
    lista = []
    while bool(n):
        n = input("Ingrese un animal o presiona enter para continuar: ")
        lista.append(n)

    print(list_animals(lista))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()