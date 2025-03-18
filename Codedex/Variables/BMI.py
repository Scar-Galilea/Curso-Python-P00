"""
Nombre: Galilea Peralta Contreras.
Fecha: 18 de marzo del 2025.

Descripción:
El índice de masa corporal (IMC) fue creado por un matemático belga en la década de 1850 y es utilizado por los profesionales de la salud y la nutrición para estimar la grasa corporal humana en ciertas poblaciones.
Se calcula tomando el peso de un individuo (masa) en kilogramos y dividiéndolo por el cuadrado de su altura en metros.

                bmi = mass/(height ** 2)

Crea un programa de BMI.py que calcule tu propio IMC.
Nota del autor: Psst. El IMC es una forma arcaica y demasiado simplificada de medir la salud personal. Fue creado por un matemático, no por un médico.
"""

def main() -> None:
    """
    Función principal.
    """

    masa_corporal = 56.0
    altura = 1.60

    bmi = masa_corporal / (altura ** 2)

    print(bmi)


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()