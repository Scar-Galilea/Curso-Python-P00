"""
Nombre: Galilea Peralta Contreras.
Fecha: 04 de mARZO del 2025.

Descripción:
El curso tiene los siguientes equipos:
    Los Algoritmos Anarquistas: Héctor, Addi y Jesús Alberto.
    Los Hackers de Café: Tania, Patricia, Rebeca.
    Los Codificadores nocturnos: Jamileth, Bryan, Rosalinda.
    Los Ctrl+Z: Galilea, Jennifer, Juan.
Este programa debe generar 6 nuevos equipos de 2 personas cada uno, pero con la restricción de que no puede haber dos personas que ya estuvieron en el mismo equipo de arriba ☝️.
"""
from random import random


def generar_equipos() -> None:
    """
    Función que genera equipos y muestra.

    """
    equipos = []
    lista = ["Hector","Addi","Jesus Aberto","Patricia","Tania","Rebeca","Jamileth","Bryan","Rosalinda","Galilea","Jennifer","Juan"]
    nombre = random.choice(lista)
    equipos.append(nombre)
    lista.remove(nombre)

    i = 0
    while i < 6:
        nombre = random.choice(lista)
        if equipos[i+i] == "Hector" or equipos[i+i] == "Addi" or equipos[i+i] == "Jesus Aberto":
            if nombre != "Hector" or nombre != "Addi" or nombre != "Jesus Aberto":
                equipos.append(nombre)
                lista.remove(nombre)
                i += 1
        elif equipos[i+i] == "Patricia" or equipos[i+i] == "Tania" or equipos[i+i] == "Rebeca":
            if nombre != "Patricia" or nombre != "Tania" or nombre != "Rebeca":
                equipos.append(nombre)
                lista.remove(nombre)
                i += 1
        elif equipos[i+i] == "Jamileth" or equipos[i+i] == "Bryan" or equipos[i+i] == "Rosalinda":
            if nombre != "Jamileth" or nombre != "Bryan" or nombre != "Rosalinda":
                equipos.append(nombre)
                lista.remove(nombre)
                i += 1
        else:
            if nombre != "Galilea"or nombre != "Jennifer" or nombre != "Juan":
                equipos.append(nombre)
                lista.remove(nombre)
                i += 1
        nombre = random.choice(lista)
        equipos.append(nombre)
        lista.remove(equipos[-1])
    k = 0
    while k < 6:
        print(f"Equipo {k + 1}")
        print(f"{equipos[i+i]},{equipos[i+1]}" )
        print()


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