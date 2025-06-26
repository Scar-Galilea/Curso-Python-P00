"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de mayo del 2025.

Descripción:
Completa la solución para que divida la cuerda en pares de dos caracteres. Si la cadena contiene un número impar de caracteres, entonces debe reemplazar el segundo personaje que falta del par final con un subrayado ('o').

Ejemplos:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

"""

def solution(s):
    lista = []
    palabra = ""
    b = False
    if len(s) % 2 != 0 and len(s) > 0:
        s = s + "_"
    for i in s:
        palabra += i
        if len(palabra) % 2 == 0:
            lista.append(palabra)
            palabra = ""
    return lista

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(solution(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()