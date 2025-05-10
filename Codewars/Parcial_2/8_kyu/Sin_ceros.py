"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Los números que terminan en cero son aburridos.
Puede que sean divertidos en tu mundo, pero no aquí.
Deshazte de ellos. Solo de los finales.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
0 -> 0
Nota: El cero debe dejarse como está.
"""

def no_boring_zeros(n: int)-> int:
    """
    Elimina ceros al final de un número entero, pero no modifica si el número es 0.
    :param n: Número entero de entrada.
    :return: Mismo número sin ceros finales.
    """
    n = str(n)
    cont = 0
    for i in n:
        if i == '0':
            cont += 1
        else:
            cont = 0
    cont = cont * - 1
    if n == "0" or n == "":
        return 0
    elif n[-1] != "0":
        return int(n)
    else:
        return int(n[0:cont])

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
    n = input("Ingrese un número: ")  # Solicita la entrada del usuario.
    n = cadena_a_entero(n)

    while n is None:
        n = input(f"Vuelve intentarlo: ")
        n = cadena_a_entero(n) # Solicita la entrada del usuario.
    print(no_boring_zeros(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()