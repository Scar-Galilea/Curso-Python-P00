"""
Nombre: Galilea Peralta Contreras.
Fecha: 06 de marzo del 2025.

Descripción:
You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.

    Your function will accept three arguments:
    The first and second argument should be numbers.
    The third argument should represent a sign indicating the operation to perform on these two numbers.

if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.
Example:

calculator(1, 2, '+') => 3
calculator(1, 2, '$') # result will be "unknown value"

"""
def calculator(x:str , y: str , op: str) -> float | str | int:

    total = "unknown value"
    if x.isnumeric() and y.isnumeric():
        x = int(x)
        y = int(y)

        if op == "+":
            total = x+y
        elif op == "-":
            total = x-y
        elif op == "*":
            total = x*y
        elif op == "/":
            total = x/y
    return int(total)

def main() -> None:
    """
    Función principal.
    """
    print("***      Calculadora  ***")
    x = input(f"x: ")
    y = input(f"y: ")
    op = input(f"Ingrese la operación a realizar: ")

    print(calculator(x,y,op))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()