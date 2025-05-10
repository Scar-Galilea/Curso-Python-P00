"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Su jefe decidió ahorrar dinero comprando algún software de reconocimiento óptico de frecuencia cortada para escanear en el texto de las novelas antiguas en su base de datos. Al principio parece capturar las palabras bien, pero rápidamente te das cuenta de que arroja muchos números a lugares al azar en el texto.
Ejemplos (avance de entrada - salida)

'!!' --> '!!'
'123456789'> ''
'This looks5 grea8t!' -> 'This looks great!'

Sus compañeros de trabajo acosados están buscándole una solución para tomar este texto confuso y eliminar todos los números. Su programa tomará una cuerda y limpiará todos los personajes numéricos, y devolverá una cuerda con espaciamiento y caracteres especiales ~#$%^&!@*():? Todos intactos.

"""

def string_clean(s: str) -> str:
    """
    Elimina los números que se encuentre en el texto.
    :param s: Cadena del usuario.
    :return: Cadena sin números.
    """
    total = ""
    for i in s:
        if not i.isnumeric():
            total = total + i
    return total

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese una oración: ") # Solicita la entrada del usuario.
    print(string_clean(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()