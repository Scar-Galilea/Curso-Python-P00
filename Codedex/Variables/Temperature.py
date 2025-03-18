"""
Nombre: Galilea Peralta Contreras.
Fecha: 18 de marzo del 2025.

Descripción:
Cree un programa de temperatura.py que convierte un número de Fahrenheit a Celsius (oC).

Utilice la siguiente fórmula y escríbala en Python:
            Celsius=(Fahrenheit−32)/1.8

Imprime la temperatura convertida. -
"""

def main() -> None:
    """
    Función principal.
    """
    # Temperatura que marca google
    fahrenheit = 60

    celsius = (fahrenheit-32)/1.8

    # La función round sirve para redondear un número.
    celsius = round(celsius)
    print(f"La temperatura {fahrenheit} fahrenheit en celsius es: {celsius}")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()