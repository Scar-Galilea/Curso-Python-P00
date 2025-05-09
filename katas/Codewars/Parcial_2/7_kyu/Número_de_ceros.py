"""
Nombre: Galilea Peralta Contreras.
Fecha: 09 de abril del 2025.

Descripción:
Crear un algoritmo para contar el número de ceros que aparecen entre 1 y N.
Ejemplos

 10  -->   1  // 10
 20  -->   2  // 10, 20
100  -->  11  // 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
200  -->  31

"""
def count_zeros(x):
    num_ceros = 0
    i = 1
    while i <= int(x):
        num_ceros += str(i).count('0')
        i += 1
    return num_ceros

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese una frase: ") # Solicita la entrada del usuario.
    print(count_zeros(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()