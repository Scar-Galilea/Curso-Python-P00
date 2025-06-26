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
    # Validar caracteres permitidos
    validos = "0123456789.+-*$"
    for c in expression:
        if c not in validos:
            return "400: Bad request"

    # Separar números y operadores
    numeros = []
    operadores = []
    numero = ""
    i = 0
    while i < len(expression):
        c = expression[i]
        if c in "0123456789.":
            numero += c
        elif c in "+-*$":
            if numero == "":
                return "400: Bad request"
            punto = 0
            for j in range(len(numero)):
                if numero[j] == ".":
                    punto += 1
                elif numero[j] not in "0123456789":
                    return "400: Bad request"
            if punto > 1:
                return "400: Bad request"
            numeros.append(float(numero))
            operadores.append(c)
            numero = ""
        i += 1

    if numero == "":
        return "400: Bad request"
    punto = 0
    for j in range(len(numero)):
        if numero[j] == ".":
            punto += 1
        elif numero[j] not in "0123456789":
            return "400: Bad request"
    if punto > 1:
        return "400: Bad request"
    numeros.append(float(numero))

    if len(numeros) != len(operadores) + 1:
        return "400: Bad request"

    # Resolver operaciones por orden: $ -> * -> - -> +
    i = 0
    while i < len(operadores):
        if operadores[i] == "$":
            if numeros[i + 1] == 0:
                return "400: Bad request"
            resultado = numeros[i] / numeros[i + 1]
            numeros[i] = resultado
            # Eliminar número siguiente
            j = i + 1
            while j < len(numeros) - 1:
                numeros[j] = numeros[j + 1]
                j += 1
            numeros.pop()
            # Eliminar operador
            j = i
            while j < len(operadores) - 1:
                operadores[j] = operadores[j + 1]
                j += 1
            operadores.pop()
        else:
            i += 1

    i = 0
    while i < len(operadores):
        if operadores[i] == "*":
            resultado = numeros[i] * numeros[i + 1]
            numeros[i] = resultado
            j = i + 1
            while j < len(numeros) - 1:
                numeros[j] = numeros[j + 1]
                j += 1
            numeros.pop()
            j = i
            while j < len(operadores) - 1:
                operadores[j] = operadores[j + 1]
                j += 1
            operadores.pop()
        else:
            i += 1

    i = 0
    while i < len(operadores):
        if operadores[i] == "-":
            resultado = numeros[i] - numeros[i + 1]
            numeros[i] = resultado
            j = i + 1
            while j < len(numeros) - 1:
                numeros[j] = numeros[j + 1]
                j += 1
            numeros.pop()
            j = i
            while j < len(operadores) - 1:
                operadores[j] = operadores[j + 1]
                j += 1
            operadores.pop()
        else:
            i += 1

    i = 0
    while i < len(operadores):
        if operadores[i] == "+":
            resultado = numeros[i] + numeros[i + 1]
            numeros[i] = resultado
            j = i + 1
            while j < len(numeros) - 1:
                numeros[j] = numeros[j + 1]
                j += 1
            numeros.pop()
            j = i
            while j < len(operadores) - 1:
                operadores[j] = operadores[j + 1]
                j += 1
            operadores.pop()
        else:
            i += 1

    return str(numeros[0])

def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(calculate(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()