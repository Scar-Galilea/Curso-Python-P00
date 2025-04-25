"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Escribe una función que absorbe una cadena binaria y devuelve el texto decodificado equivalente (el texto está codificado ASCII).

Cada 8 bits en la cadena binaria representan 1 caracteres en la tabla ASCII.

La cadena de entradas siempre será una cadena binaria válida.

Los personajes pueden estar en el rango de "00000000" a "11111111" (inclusive)

Nota: En el caso de una cadena binaria vacía su función debe devolver una cadena vacía.

"""

def binary_to_string(binario:str):
    n = len(binario)
    a = 0
    b = 8
    palabra = ""
    while a < n:
        bit=int(binario[a:8+1])

        Acumulador_binario = ""
        while bit // 2 != 0:
            Acumulador_binario = str(bit % 2) + Acumulador_binario
            bit = bit // 2
        n= str(bit) + Acumulador_binario


        palabra = palabra + chr(int(n))
        a += 8
        b += 8

    return palabra

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.

    print(binary_to_string(n))
    print(int(n[0:8]))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()