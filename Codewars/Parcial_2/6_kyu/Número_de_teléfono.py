"""
Nombre: Galilea Peralta Contreras.
Fecha: 22 de abril del 2025.

Descripción:
Escriba una función que acepte una cadena, y devuelve la verdad si está en forma de número de teléfono.
Supongamos que cualquier entero de 0-9 en cualquiera de los spots producirá un número de teléfono válido.

Sólo se preocupa por el siguiente formato:
(123) 456-7890 (no olvides el espacio después de los paréntesis cercanos)

Ejemplos:

"(123) 456-7890"  => true
"(1111)555 2345"  => false
"(098) 123 4567"  => false

"""
def valid_phone_number(phone_number):
    a = "(123) 456-7890"
    b = True
    for i,k in zip(phone_number,a):
        if not (i.isnumeric() and k.isnumeric()):
            if not i == k:
                b = False
                break
    return b



def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese: ") # Solicita la entrada del usuario.
    print(valid_phone_number(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()