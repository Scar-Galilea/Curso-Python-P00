"""
Nombre: Galilea Peralta Contreras.
Fecha: 07 de abril del 2025.

Descripción:
mplementar String#to_cents, que debe analizar los precios expresados como $1.23y número de retorno de centavos, o en caso de devolución de mal formato nil.

En esta kata, por un precio a considerar válido, debe comenzar con un signo de dólar ($), seguido inmediatamente por un número decimal con exactamente 2 dígitos decimales.
"""

def to_cents(amount:str) -> int | None:
    no_puntos = amount.count(".")
    no_signo = amount.count("$")
    revisar_cadena = amount.lstrip('.').replace(".","")
    revisar_cadena = revisar_cadena.lstrip('$')
    if revisar_cadena.isnumeric() and no_puntos in (1,1) and no_signo in (1,1) and amount[-3] == '.':
        return int(revisar_cadena)
    else:
        return None






def main() -> None:
    """
    Función principal.
    """

    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(to_cents(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()