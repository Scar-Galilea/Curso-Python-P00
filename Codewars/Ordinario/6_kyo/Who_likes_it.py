"""
Nombre: Galilea Peralta Contreras.
Fecha: 25 junio del 2025.

Descripción:
Probablemente conozcas el sistema de "me gusta" de Facebook y otras páginas. La gente puede darle "me gusta" a publicaciones de blogs, fotos u otros elementos. Queremos crear el texto que debe aparecer junto a cada elemento.

Implementa la función que toma un array con los nombres de las personas a las que les gusta un artículo. Debe devolver el texto mostrado, como se muestra en los ejemplos:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Nota: Para 4 o más nombres, el número "and 2 others"simplemente aumenta.
"""

def likes(names):
    """
    Función que recibe una lista de nombres de personas que han dado 'like' a un contenido
    y devuelve una cadena con un mensaje dependiendo del número de nombres.
    """
    cantidad = len(names)

    if cantidad == 0:
        return "no one likes this"
    elif cantidad == 1:
        return f"{names[0]} likes this"
    elif cantidad == 2:
        return f"{names[0]} and {names[1]} like this"
    elif cantidad == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        otros = cantidad - 2
        return f"{names[0]}, {names[1]} and {otros} others like this"

def main() -> None:
    """
    Función principal.
    """
    print(likes([]))
    print(likes(["Peter"]))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()