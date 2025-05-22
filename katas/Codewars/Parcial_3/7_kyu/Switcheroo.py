"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de mayo del 2025.

Descripción:
Escriba una función que tome una cadena y reemplace todas las letras con sus respectivas posiciones en el alfabeto inglés; por ejemplo. 'a'es 1, 'z'es 26. La función debe ser insensible.

'abc'      --> '123'
'ABC'      --> '123'
'codewars' --> '315452311819'
'abc-#@5'  --> '123-#@5'

"""

def encode(st):
    total = ""
    letras = {"a":"1",
              "b":"2",
              "c": "3",
              "d": "4",
              "e": "5",
              "f": "6",
              "g": "7",
              "h": "8",
              "i": "9",
              "j": "10",
              "k": "11",
              "l": "12",
              "m": "13",
              "n": "14",
              "o": "15",
              "p": "16",
              "q": "17",
              "r": "18",
              "s": "19",
              "t": "20",
              "u": "21",
              "v": "22",
              "w": "23",
              "x": "24",
              "y": "25",
              "z": "26",
              }
    for i in st:
        total += letras.get(i.lower(),i)
    return total

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(encode(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()