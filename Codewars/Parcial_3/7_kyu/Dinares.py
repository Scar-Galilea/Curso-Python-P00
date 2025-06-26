"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de mayo del 2025.

Descripción:
Determinar el número total de dígitos en el número entero (n>=0) dado como entrada a la función. Por ejemplo, 9 es un solo dígito, 66 tiene 2 dígitos y 128685 tiene 6 dígitos. Tenga cuidado de evitar desbordamientos/flujos.
Todas las entradas serán válidas.

"""

def digits(n):
    return len(str(n))

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(digits(n))


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()