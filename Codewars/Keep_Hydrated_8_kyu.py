"""
Nombre: Galilea Peralta Contreras.
Fecha: 06 de marzo del 2025.

Descripción:
Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.

For example:
time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
"""
def litres(time:float) -> int:
    """
    Calcular los litros.
    :param lts: litros.
    :return: Los litros que ocupará para el ejercicio.
    """
    lts = time * 0.5

    return int(lts)

def cadena_a_flotante(cadena: str) -> float | None:
    """
    Convertir una cadena a flotante.
    :return: Un número flotantes o none.
    """
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".", "")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None


def main() -> None:
    """
    Función principal.
    """
    time = input(f"Tiempo de ejercicio: ")
    time = cadena_a_flotante(time)

    while time == None:
        time = input(f"Vuelve intentarlo: ")
        time = cadena_a_flotante(time)


    print(f"time = {time} ----> litres = {litres(time)}")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()