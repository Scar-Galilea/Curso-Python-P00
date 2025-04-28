"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Definir una función que elimine los duplicados de una serie de números no negativos y lo devuelva como resultado.
El orden de la secuencia tiene que mantenerse igual.

Ejemplos:
Input -> Output
[1, 1, 2] -> [1, 2]
[1, 2, 1, 1, 3, 2] -> [1, 2, 3]


"""

def distinct(seq:list[int])->list[int]:
    lista = [seq[0]]
    for i in seq:
        if i not in lista:
            lista.append(i)
    return lista


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(distinct(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()