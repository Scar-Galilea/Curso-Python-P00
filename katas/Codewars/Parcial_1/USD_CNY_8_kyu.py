"""
Nombre: Galilea Peralta Contreras.
Fecha: 31 de marzo del 2025.

Descripción:
Create a function that converts US dollars (USD) to Chinese Yuan (CNY) . The input is the amount of USD as an integer, and the output should be a string that states the amount of Yuan followed by 'Chinese Yuan'
Examples (Input -> Output)

15  -> '101.25 Chinese Yuan'
465 -> '3138.75 Chinese Yuan'

The conversion rate you should use is 6.75 CNY for every 1 USD. All numbers should be represented as a string with 2 decimal places. (e.g. "21.00" NOT "21.0" or "21")

"""

def usdcny(usd:float)-> str :
    """
    Convierte la cantidad de dólares estadounidenses (USD) a yuanes chinos (CNY) utilizando una tasa de cambio de 6.75.
    :param usd: La cantidad en dólares estadounidenses a convertir.
    :return: Una cadena que contiene la cantidad de yuanes chinos con dos decimales seguidos de 'Chinese Yuan'.
    """
    return f"{(usd*6.75):.2f} Chinese Yuan"

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
    # Solicita al usuario la cantidad de dólares que desea convertir.
    usd = (input("Ingrese los dolares: "))
    usd = cadena_a_entero(usd)

    while usd is None:
        usd = input(f"Vuelve intentarlo los parametros: ")
        usd = cadena_a_entero(usd)

    print(usdcny(usd))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()