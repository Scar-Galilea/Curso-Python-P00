"""
Nombre: Galilea Peralta Contreras.
Fecha: 31 de marzo del 2025.

Descripción:

"""

def count_arara(n:int) -> str | None:
    impar = "anane"
    par = ""
    if n%2== 0 and n<= 8: return par*n
    elif n%2!= 0 and n<= 8 :return impar*(n-1)

def cadena_a_entero(cadena: str) -> int | None:
    """
       Muestra el menu del programa
       :param cadena: Lo que ingresa el usuario
       :return: Un número entero o None
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

    n = input("Ingrese el número de parejas de la tribu Arara ")
    n = cadena_a_entero(n)
    while n is None:
        n = input(f"Vuelve intentarlo: ")
        n = cadena_a_entero(n)

    print(count_arara(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()