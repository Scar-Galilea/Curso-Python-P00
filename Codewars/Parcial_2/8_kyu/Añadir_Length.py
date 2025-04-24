"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Y si necesitamos que la longitud de las palabras separadas por un espacio se añada al final de esa misma palabra y que haya devuelto como una matriz?

Ejemplo de esto (aportación --avaja)
"apple ban" --> ["apple 5", "ban 3"]
"you will win" -->["you 3", "will 4", "win 3"]

Su tarea es escribir una función que tome una cuerda y devuelva una lista de Array con la longitud de cada palabra añadida a cada elemento.
Nota: La cuerda tendrá al menos un elemento; las palabras siempre estarán separadas por un espacio.

"""

def add_length(str_:str)-> list[str]:
    cont = 0
    rango = str_.split()
    lista = []
    aux = 0
    for i in str_:
        cont += 1
        if i == " ":
            palabras = rango[aux:cont]
            print(palabras)
            aux = cont
        https: // www.codewars.com / kata / 559
        d2284b5bb6799e9000047 / train / python


    return lista

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(add_length(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()