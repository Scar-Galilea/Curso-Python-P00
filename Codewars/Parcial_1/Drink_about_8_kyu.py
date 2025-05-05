"""
Nombre: Galilea Peralta Contreras.
Fecha: 31 de marzo del 2025.

Descripción:
    Kids drink toddy.
    Teens drink coke.
    Young adults drink beer.
    Adults drink whisky.

Make a function that receive age, and return what they drink.

Rules:
    Children under 14 old.
    Teens under 18 old.
    Young under 21 old.
    Adults have 21 or more.

Examples: (Input --> Output)

13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"
"""
def people_with_age_drink(age: int) -> str | None:
    """
    Determina la bebida correspondiente según la edad de la persona.
    :param age: Edad de la persona.
    :return: Una cadena indicando la bebida correspondiente.
    """
    if age <= 13:
        return "drink toddy"  # Menores de 14 años beben toddy.
    elif age < 18:
        return "drink coke"  # Menores de 18 años beben coca-cola.
    elif age < 21:
        return "drink beer"  # Menores de 21 años beben cerveza.
    elif age >= 21:
        return "drink whisky"  # 21 años o más beben whisky.

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

    age  = input("Ingrese su edad: ") # Solicita la edad al usuario.
    age = cadena_a_entero(age)
    while age is None:  # Valida que la entrada sea un número válido.
        age = input(f"Vuelve intentarlo: ")
        age = cadena_a_entero(age)

    print(people_with_age_drink(age)) # Muestra la bebida correspondiente.


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()