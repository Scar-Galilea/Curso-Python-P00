"""
Nombre: Galilea Peralta Contreras.
Fecha: 07 de abril del 2025.

Descripción:
¿Implementar String#digit? (en Java StringUtils.isDigit(String)),
que debería regresar true si el objeto dado es un solo dígito (0-9), false de otra manera.


"""
def is_digit(n:str) -> bool:
    """
    Verifica si una cadena representa un único dígito decimal entre 0 y 9.
    :param n: Cadena a verificar.
    :return: True si es un solo dígito (0-9), False en cualquier otro caso.
    """

    # Verifica si todos los caracteres de la cadena son numéricos (0-9).
    if n.isnumeric():
        n1 = n
        n = int(n)
        # Si tiene más de un dígito Y empieza con '0', se considera inválido.
        if len(n1) >= 2 and n1[0] == '0':
            return False
        # Verifica que el número esté en el rango de 0 a 9.
        if 9 >= n >= 0:
            return True
        else:
            return False
    else:
        # Si la cadena contiene letras, espacios u otros caracteres no numéricos.
        return False


def main() -> None:
    """
    Función principal.
    """
    n = input("Ingrese una cadena: ") # Solicita la entrada del usuario.
    print(is_digit(n))



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
