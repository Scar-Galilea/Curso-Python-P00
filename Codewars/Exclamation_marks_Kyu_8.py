"""
Nombre: Galilea Peralta Contreras.
Fecha: 31 de marzo del 2025.

Descripción:

 Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
Examples

"Hi!" --> "H!!"
"!Hi! Hi!" --> "!H!! H!!"
"aeiou" --> "!!!!!"
"ABCDE" --> "!BCD!"

"""
def replace_exclamation(st:str) -> str:
    """
    Función que reemplaza todas las vocales en una cadena por '!'
    :param st: Cadena de entrada.
    :return: Cadena modificada con las vocales reemplazadas por '!'
    """
    st2 = ''  # Inicializa una nueva cadena vacía donde se almacenará el resultado.
    # Recorre cada caracter de la cadena original
    for i in st:
        # Verifica si el caracter es una vocal (minúscula o mayúscula).
        if i.lower() == 'a' or i.lower() == 'e' or  i.lower() == 'i' or i.lower() == 'o' or i.lower() == "u":
            st2 = st2 + '!' # Sustituye la vocal por '!'.
        else:
            st2 = st2 + i # Mantiene el caracter sin cambios si no es una vocal.
    return st2



def main() -> None:
    """
    Función principal.
    """
    st = input("Ingrese una frase: ") # Solicita la entrada del usuario.
    print(replace_exclamation(st))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()