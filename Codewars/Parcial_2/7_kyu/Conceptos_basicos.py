"""
Nombre: Galilea Peralta Contreras.
Fecha: 07 de abril del 2025.

Descripción:
Implementar String#to_cents, que debe analizar los precios expresados como $1.23y número de retornos de centavos, o en caso de devolución de mal formato nil.
En esta kata, por un precio a considerar válido, debe comenzar con un signo de dólar ($), seguido inmediatamente por un número decimal con exactamente 2 dígitos decimales.
"""

def to_cents(amount:str) -> int | None:
    """
    Convierte un precio dado como string (por ejemplo, "$1.23") a centavos como entero (123).
    Si el formato es inválido, retorna None.
    :param amount: Cadena que representa un precio en dólares.
    :return: Precio en centavos como entero o None si el formato no es válido.
    """
    # Cuenta cuántos puntos.
    no_puntos = amount.count(".")

    # Cuenta cuántos signos de dólar.
    no_signo = amount.count("$")

    revisar_cadena = amount.lstrip('.').replace(".","")

    # Elimina el símbolo de dólar si está al inicio.
    revisar_cadena = revisar_cadena.lstrip('$')

    # Verifica que el contenido restante (sin puntos ni $) sea numérico.
    if revisar_cadena.isnumeric() and no_puntos in (1,1) and no_signo in (1,1) and amount[-3] == '.':
        return int(revisar_cadena)
    else:
        return None


def main() -> None:
    """
    Función principal.
    """

    n = input("Ingrese un precio en dollars: ") # Solicita la entrada del usuario.
    print(to_cents(n))


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()