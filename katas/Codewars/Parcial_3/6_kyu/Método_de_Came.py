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

def camel_case(s:str)->str:
    r = ""
    if len(s) > 0:
        r = s[0].upper()
        for i in range(1,len(s)):
            if s[i-1] == " ":
                r += s[i].upper()
            else:
                r += s[i]
        r = r.replace(" ", "")
    return r


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(camel_case(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()