"""
Nombre: Galilea Peralta Contreras.
Fecha: 08 de abril del 2025.

Descripción:
Implementar String#whitespace?(str)(Ruby),
String.prototype.whitespace(str)(JavaScript),
String::whitespace(str)(CoffeeScript), o whitespace(str)(Python),
que debería regresar true/Truesi el objeto dado consiste exclusivamente en caracteres de espacio cero o más,
false/Falsede otra manera.

"""

def whitespace(string:str)-> bool:
    revisar_cadena = string.replace("\n","").replace("\r","").replace("\t","").strip()
    if len(revisar_cadena)!=0:
        return False
    else:
        return True

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese una frase: ") # Solicita la entrada del usuario.
    print(whitespace(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()