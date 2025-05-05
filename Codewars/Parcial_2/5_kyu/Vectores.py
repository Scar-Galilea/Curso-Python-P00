"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Cree una función, que acepte un número arbitrario de arrays y devuelva una sola matriz generada por la alternativa anexando elementos de los argumentos pasados. Si uno de ellos es más corto que los demás, el resultado debe acolcharse con elementos vacíos.

Ejemplos:

interleave([1, 2, 3], ["c", "d", "e"]) == [1, "c", 2, "d", 3, "e"]
interleave([1, 2, 3], [4, 5]) == [1, 4, 2, 5, 3, None]
interleave([1, 2, 3], [4, 5, 6], [7, 8, 9]) == [1, 4, 7, 2, 5, 8, 3, 6, 9]
interleave([]) == []

"""

def interleave(*args):
    total = []
    m = 0
    for i in args:
        if len(i) > m:
            m = int(len(i))

    for k in range(m):
        for i in args:
            if k < len(i):
                total.append(i[k])
            else:
                total.append(None)
    return total



def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(interleave(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()