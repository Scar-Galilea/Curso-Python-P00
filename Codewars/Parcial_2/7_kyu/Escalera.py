"""
Nombre: Galilea Peralta Contreras.
Fecha: 10 de abril del 2025.

Descripción:
Usando ncomo parámetro en la función pattern, dónde n > 0, complete el código para obtener el patrón:

1
1*2
1**3
1***4
... and so on...

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
def pattern(n: int)-> None:
    asteriscos = "*"
    total = "1"
    salto = "\n"
    for i in range(1,n):
        total = total + salto + "1" + asteriscos + str(i+1)
        asteriscos += "*"
    return total

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese una frase: ") # Solicita la entrada del usuario.
    print(pattern(int(n)))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()