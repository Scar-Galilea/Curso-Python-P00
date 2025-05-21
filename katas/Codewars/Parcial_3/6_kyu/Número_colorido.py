"""
Nombre: Galilea Peralta Contreras.
Fecha: 20 de mayo del 2025.

Descripción:
scriba un método (o función, dependiendo del idioma) que convierta una cadena en camelloCase, es decir, todas las palabras deben tener su primera letra capitalizada y los espacios deben ser eliminados.
Ejemplos (avance de entrada --o:

"hello case" --> "HelloCase"
"camel case word" --> "CamelCaseWord"

No te olvides de calificar esta kata. Gracias:)
"""

def colorful(number):
    if len(str(number)) == 1:
        return True
    else:
        lista = []
        lista_1 = []
        total = 1
        b = True
        for i in str(number):
            lista_1.append(int(i))
            total *= int(i)

        for k in range(len(str(number))-1):
            lista.append(lista_1[k] * lista_1[k+1])

        lista.append(total)

        for i in lista_1:
            if i in lista:
                b = False
                break
        return b

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(colorful(int(n)))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()