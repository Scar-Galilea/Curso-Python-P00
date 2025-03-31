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
    st2 =  None
    for i in st:
        if i.lower() == ('a','e','i','o','u'):
            print()
            st2 = st2 + '!'
        else:
            st2 = st2 + i
    return st2




def main() -> None:
    """
    Función principal.
    """

    st = input("Ingrese una cadena: ")
    replace_exclamation(st)





""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()