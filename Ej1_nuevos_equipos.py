"""
Nombre: Galilea Peralta Contreras.
Fecha: 04 de marzo del 2025.

Descripción:
El curso tiene los siguientes equipos:
    Los Algoritmos Anarquistas: Héctor, Addi y Jesús Alberto.
    Los Hackers de Café: Tania, Patricia, Rebeca.
    Los Codificadores nocturnos: Jamileth, Bryan, Rosalinda.
    Los Ctrl+Z: Galilea, Jennifer, Juan.
Este programa debe generar 6 nuevos equipos de 2 personas cada uno, pero con la restricción de que no puede haber dos personas que ya estuvieron en el mismo equipo de arriba ☝️.
"""
import random


def generar_equipos() -> None:
    """
    Función que genera equipos y muestra.
    """
    equipo_anteriores = [["Hector","Addi","Jesus Aberto"],["Patricia","Tania","Rebeca"],["Jamileth","Bryan","Rosalinda"],["Galilea","Jennifer","Juan"]]
    participantes = []
    equipos_nuevos = []

    for i in equipo_anteriores:
        for k in i:
            participantes.append(k)

    estudiante = random.choice(participantes)
    equipos_nuevos.append(estudiante)
    participantes.remove(estudiante)

    while len(participantes) > 2:
        estudiante = random.choice(participantes)
        for i in equipo_anteriores:
            contador = 0
            for k in i:
                if estudiante != k:
                    contador += 1
            if contador == 3:
                equipos_nuevos.append(estudiante)
                participantes.remove(estudiante)
                break

        estudiante = random.choice(participantes)
        equipos_nuevos.append(estudiante)
        participantes.remove(estudiante)

    equipos_nuevos.append(participantes[0])

    k = 0

    while k < 6:
        print(equipos_nuevos[k+k*1],equipos_nuevos[k+1+1*k])
        k += 1







def main() -> None:
    """
    Función principal.
    """

    print("********  Generar nuevos equipos para el semestre. ********")
    print()
    generar_equipos()


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()