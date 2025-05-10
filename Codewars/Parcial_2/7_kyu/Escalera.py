"""
Nombre: Galilea Peralta Contreras.
Fecha: 10 de abril del 2025.

Descripción:
Usando n como parámetro en la función pattern, dónde n > 0, complete el código para obtener el patrón:

1
1*2
1**3
1***4

Nota: No hay nueva línea al final (después de los fines del patrón).
Ejemplos

pattern(3)debe regresar "1\n1*2\n1**3", por ejemplo, lo siguiente:

1
1*2
1**3

pattern(10):deberá devolver lo siguiente:

1
1*2
1**3
1***4
1****5
1*****6
1******7
1*******8
1********9
1*********10

"""
def pattern(n: int)-> None | str:
    """
    Genera un patrón de texto creciente con asteriscos y números.
    :param n: Número de líneas del patrón.
    :return: Cadena con el patrón generado o None si 'n' no es válido.
    """
    asteriscos = "*"
    total = "1"
    salto = "\n"

    # Se inicia el bucle desde 1 hasta n-1 para agregar las líneas restantes.
    for i in range(1,n):
        total = total + salto + "1" + asteriscos + str(i+1)
        asteriscos += "*"
    return total

def cadena_a_entero(cadena: str) -> int | None:
    """
    Muestra el menu del programa.
    :param cadena: Lo que ingresa el usuario.
    :return: Un número entero o None.
    """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in(0,1) :
        return  int(cadena)
    else:
        return None

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese una frase: ") # Solicita la entrada del usuario.

    n = cadena_a_entero(n)

    while n is None:
        n = input(f"Vuelve intentarlo: ")
        n = cadena_a_entero(n)

    print(pattern(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()