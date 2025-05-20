"""
Nombre: Galilea Peralta Contreras.
Fecha: 20 de mayo del 2025.

Descripción:
Esta calculadora toma valores que podrían escribirse en un camino de la ruta de los navegadores como una sola cadena. A continuación, devuelve el resultado como un número (o un mensaje de error).

Las rutas utilizan el símbolo '/' para que esto no pueda estar en nuestra calculadora. En su lugar estamos usando el símbolo '$' como nuestro operador de división.

Se le pasará una serie de cualquier longitud que contenga números y operadores:

    'Añadir
    '-' = restar
    '*' = multiplicar
    '$' = división

Su tarea es romper la cadena y calcular la expresión usando este orden de operaciones. (división =-multicradura =- rest =- adición)

Si se le da una entrada inválida (es decir, cualquier carácter excepto .0123456789+-*$) debe devolver el mensaje de error:'400: Bad request'
Recuerde:

    El número de operaciones no es limitado
    Orden de operaciones es imperativo
    No, no evalo funciones equivalentes
    convertir el número en floats, no a los enteros

Ejemplos:

calculate('1+1')     => '2'
calculate('10$2')    => '5'
calculate('1.5*3')   => '4.5'

calculate('5+5+5+5') => '20'

calculate('1000$2.5$5+5-5+6$6') =>'81'

calculate('10-9p')   =>  '400: Bad request'

Notas adicionales - Parámetros fuera de este desafío:

    Brackets, por ejemplo. 10* ((1 2)
    Raíz cuadrada, log, % o cualquier otro operador
    Unary menos (10*-1)
    Mala entrada matemática (10**$10 o 5$5$)
    Puede que tengas que lidiar con flotas.

Si disfrutas de esto y quieres algo más difícil, por favor vea http://www.codewars.com/kata/evaluate-matemática-expresión/ para hacer una calculadora mucho más complicada. Esta es una buena kata que lleva a eso.

"""
def calculate(expression):
    total = 0
    numero = []
    cont = 0
    n = ""
    for i in expression:
        if i.isnumeric():
            n += i
        elif i != ".":
            numero.append(int(n))
            n = ""

    for i in expression:
        if i.isnumeric():
            pass
        elif i == "+":
            total += numero[cont] + numero[cont+1]
            cont += 1
        elif i == "-":
            total += numero[cont] - numero[cont+1]
            cont += 1
        elif i == "*":
            total += numero[cont] * numero[cont+1]
            cont += 1
        elif i == "$":
            total += numero[cont] * numero[cont+1]
            cont += 1
        elif i.isnumeric() or i == ".":
            pass
        else:
            total = "400: Bad request"
            break

    if len(n) <= 1:
        total = int(expression)

    return total


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(calculate(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()