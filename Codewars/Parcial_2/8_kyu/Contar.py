"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Lleva a tu hijo al bosque para ver a los monos. Usted sabe que hay un cierto número allí (n), pero su hijo es demasiado joven para apreciar el número completo, él tiene que empezar a contarlos desde 1.
Como buen padre, te sentarás y contarás con él. Dado el número (n), pueblan una matriz con todos los números hasta e incluyendo ese número, pero excluyendo cero.

Por ejemplo: "Aportación" --abaja:

10 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 1 --> [1]
"""

def monkey_count(n:str) -> list[int]:
    """
    Genera una lista de números del 1 al n .
    :param n: Número en formato de cadena que representa la cantidad total de monos.
    :return: Lista con números enteros desde 1 hasta n.
    """

    lista = []
    for i in range(1,int(n)+1):
        lista.append(i)
    return lista


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese una palabra: ") # Solicita la entrada del usuario.
    print(monkey_count(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()