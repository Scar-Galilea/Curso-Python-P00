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
def calculator(x:str , y: int , op: str) -> float | str:

    total = None
    if op == "+":
        total = x+y
    elif op == "-":
        total = x-y
    elif op == "*":
        total = x*y
    elif op == "/":
        total = x/y
    else:
        total = "unknown value"
    return total

def cadena_a_entero(cadena: str) -> int | None:
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
    print("***      Calculadora  ***")
    x = input(f"x: ")
    y = input(f"y: ")
    op = input(f"Ingrese la operación a realizar: ")
    x = cadena_a_entero(x)
    y = cadena_a_entero(y)

    calculator(x,y,op)

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()