"""
Nombre: Galilea Peralta Contreras.
Fecha: 31 de marzo del 2025.

Descripción:
Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

For example n = 3 result in:

"I\n I\n  I"

or printed:

I
 I
  I

Another example, a 7-step stairs should be drawn like this:

I
 I
  I
   I
    I
     I
      I

"""

def draw_stairs(n:int):
    c = 'I'
    cadena = ""
    espacio = " "
    cont = 1
    for i in range(0,n - 1):
        cadena = cadena + c + "\n" + espacio * cont
        cont += 1
    cadena = cadena + c
    return cadena


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

    n = input("Ingrese el número de saltos de linea: ")
    n = cadena_a_entero(n)
    while n is None:
        n = input(f"Vuelve intentarlo: ")
        n = cadena_a_entero(n)

    print(draw_stairs(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()