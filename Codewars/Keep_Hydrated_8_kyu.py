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
    Calcula la cantidad de litros de agua que Nathan necesita beber.
    :param time: Tiempo en horas que Nathan ha estado haciendo ejercicio.
    :return: Cantidad de litros de agua (redondeado hacia abajo).
    """
    lts = time * 0.5  # Calcula la cantidad de litros de agua según las horas de ejercicio.
    return int(lts)  # Convierte el resultado a un entero para redondear.

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
    time = input("Tiempo de ejercicio (en horas): ")  # Solicita al usuario el tiempo en horas.
    time = cadena_a_flotante(time)  # Intenta convertir la entrada a flotante.

    while time is None:
        time = input("Entrada no válida. Intenta de nuevo: ")
        time = cadena_a_flotante(time)

    # Muestra el resultado de la cantidad de litros de agua que debe beber.
    print(f"time = {time} ----> litres = {litres(time)}")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()