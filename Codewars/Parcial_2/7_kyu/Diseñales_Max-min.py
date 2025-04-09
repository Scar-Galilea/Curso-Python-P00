"""
Nombre: Galilea Peralta Contreras.
Fecha: 09 de abril del 2025.

Descripción:
En esta Kata, se le dará una serie de elementos únicos, y su tarea es reorganizar los valores para que el primer valor máximo sea seguido por el primer mínimo, seguido de segundo valor máximo luego el segundo valor de segundo min, etc.
Por ejemplo:
solve([15,11,10,7,12]) = [15,7,12,10,11]

El primer máximo es 15y el primer min es 7. El segundo máximo es 12y el segundo min es 10y así sucesivamente.
Más ejemplos en los casos de prueba.
- Buena suerte.


"""

def solve(arr:list[int]):
    lista_nueva = [max(arr)]
    arr.remove(max(arr))
    i = 1

    while i < len(arr):
        lista_nueva.append(min(arr))
        arr.remove(min(arr))
        lista_nueva.append(max(arr))
        arr.remove(max(arr))

    if len(arr) == 1:
        lista_nueva.append(arr[0])
    return lista_nueva



def main() -> None:
    """
    Función principal.
    """
    i = 0
    lista = []
    while i <= 6:
        n = input("Ingrese una frase: ") # Solicita la entrada del usuario.
        lista.append(int(n))
        i += 1


    print(solve(lista))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()