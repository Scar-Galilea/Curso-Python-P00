"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Se le dará una matriz ay un valor x. Todo lo que necesita hacer es comprobar si el array proporcionado contiene el valor.
Puede contener números o cuerdas. x Puede ser cualquiera de los dos.
Regreso true si el array contiene el valor, false si no.

"""

def check(seq: list[str], elem: str) -> bool | None:
    """
    Verifica si un elemento está presente en una lista.
    :param seq: Lista de elementos (pueden ser strings o enteros).
    :param elem: Elemento a buscar dentro de la lista.
    :return: True si el elemento se encuentra, False si no.
    """
    for i in seq:
        if i == elem:
            return True
    return False


def main() -> None:
    """
    Función principal.
    """
    lista = []
    n = input("Ingrese un caracter o presiona enter para continuar: ")  # Solicita la entrada del usuario.
    lista = []

    while bool(n):
        n = input("Ingrese un animal o presiona enter para continuar: ")

        if n is None:
            print("Formato no válido, intenta nuevamente.")
        # Si el número es impar, se ignora y no se suma.
        else:
            lista.append(n)

    n1 = input("Ingrese el elemento a encontrar: ")  # Solicita la entrada del usuario.


    print(check(lista,n1))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()