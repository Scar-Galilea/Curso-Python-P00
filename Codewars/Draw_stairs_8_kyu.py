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

def draw_stairs(n:int) -> str:
    """
    Genera una cadena que representa una escalera de 'I',
    con 'n' escalones alineados a la izquierda.
    :param n: Número de escalones.
    :return: Cadena con la escalera.
    """
    c = 'I'  # Caracter que representa el escalón.
    cadena = ""  # Variable para almacenar la escalera.
    espacio = " "  # Espacio usado para el desplazamiento.
    cont = 1  # Contador para incrementar espacios.
    # Bucle que genera los primeros n-1 escalones

    for i in range(0, n - 1):
        cadena = cadena + c + "\n" + espacio * cont  # Agrega el escalón y nueva línea.
        cont += 1  # Incrementa los espacios para el siguiente nivel.

    cadena = cadena + c  # Agrega el último escalón sin nueva línea al final.
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
    Función principal que solicita al usuario un número y genera la escalera.
    """
    n = input("Ingrese el número de saltos de linea: ")
    n = cadena_a_entero(n)  # Convierte la entrada a entero

    # Mientras la entrada no sea válida, solicita de nuevo
    while n is None:
        n = input("Vuelve intentarlo: ")
        n = cadena_a_entero(n)

    print(draw_stairs(n))  # Imprime la escalera generada



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()