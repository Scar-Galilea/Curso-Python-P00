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
    """
    Elimina los elementos duplicados de una lista de enteros, conservando el orden original.
    :param seq: Lista de números enteros.
    :return: Lista sin duplicados en el mismo orden en que aparecieron.
    """
    lista = [seq[0]]
    for i in seq:
        if i not in lista:
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
    lista = []
    num_cadena = input(f"Ingresa un número  o presiona enter para continuar: ")

    while bool(num_cadena):
        # Se convierte la cadena ingresada a un número entero si es válido
        numero = cadena_a_entero(cadena=num_cadena)

        if numero is None:
            print("Formato no válido, intenta nuevamente.")
        # Si el número es impar, se ignora y no se suma.
        else:
            lista.append(numero)

        num_cadena = input(f"Ingresa un número  o presiona enter para continuar: ")

    print(distinct(lista))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()