"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Se le dará una matriz ay un valor x. Todo lo que necesita hacer es comprobar si el array proporcionado contiene el valor.
apuede contener números o cuerdas. xPuede ser cualquiera de los dos.
Regreso truesi el array contiene el valor, falseSi no.


"""

def check(seq, elem: str) -> bool | None:
    for i in seq:
        if i == elem:
            return True
    return False


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    n1 = input("Ingrese: ")  # Solicita la entrada del usuario.
    print(check(n,n1))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()