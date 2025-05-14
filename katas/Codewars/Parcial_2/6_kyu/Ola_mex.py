"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:


"""

def wave(people:str)->list[str]:
    lista = []
    for i in range(len(people)):
        palabra = ""
        cont = 0
        if people[i]!= " ":
            for k in people:
                if cont == i:
                    palabra +=  k.upper()
                else:
                    palabra += k
                cont += 1
        if len(palabra) != 0:
            lista.append(palabra)
    return lista


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(wave(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()