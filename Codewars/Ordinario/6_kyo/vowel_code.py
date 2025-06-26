"""
Nombre: Galilea Peralta Contreras.
Fecha: 25 junio del 2025.

Descripción:
Paso 1: Cree una función llamada encode()para reemplazar todas las vocales minúsculas en una cadena dada con números de acuerdo con el siguiente patrón:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
Por ejemplo, encode("hello")devolvería "h2ll4". No hay necesidad de preocuparse por las vocales mayúsculas en este kata.

Paso 2: Ahora crea una función llamada decode()para convertir los números nuevamente en vocales de acuerdo con el mismo patrón que se muestra arriba.

Por ejemplo, decode("h3 th2r2")devolvería "hi there".

Para simplificar, puedes asumir que cualquier número pasado a la función corresponderá a vocales.


"""


def encode(texto):
    resultado = ""
    for letra in texto:
        if letra == "a":
            resultado += "1"
        elif letra == "e":
            resultado += "2"
        elif letra == "i":
            resultado += "3"
        elif letra == "o":
            resultado += "4"
        elif letra == "u":
            resultado += "5"
        else:
            resultado += letra
    return resultado

def decode(texto):
    resultado = ""
    for letra in texto:
        if letra == "1":
            resultado += "a"
        elif letra == "2":
            resultado += "e"
        elif letra == "3":
            resultado += "i"
        elif letra == "4":
            resultado += "o"
        elif letra == "5":
            resultado += "u"
        else:
            resultado += letra
    return resultado


def main() -> None:
    """
    Función principal.
    """
    texto_original = "hello"
    texto_codificado = encode(texto_original)
    print("Texto codificado:", texto_codificado)  # debería imprimir: h2ll4

    texto_para_decodificar = "h3 th2r2"
    texto_decodificado = decode(texto_para_decodificar)
    print("Texto decodificado:", texto_decodificado)  # debería imprimir: hi there


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()