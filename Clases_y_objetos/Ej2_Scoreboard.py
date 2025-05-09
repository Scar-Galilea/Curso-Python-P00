"""
Nombre: Galilea Peralta Contreras.
Fecha: 11 de marzo del 2025.

Descripción:
Se necesita desarrollar un sistema que permita gestionar y visualizar un scoreboard (puntuación) dentro de una ventana gráfica. El sistema debe cumplir con los siguientes requisitos:

1. Scoreboard:

Debe almacenar y gestionar la puntuación actual,
Debe permitir actualizar la posición,
Debe ser capaz de dibujarse en pantalla con un formato específico.

"""

class Scoreboard:
    def __init__(self,points : int = 0,text_color: tuple[int,int,int] = (0,0,0),font: str = 'Kimono',size: float = 48):
        """
        Constructor de la clase Scoreboard.
        :param points: Puntuación inicial.
        :param text_color: Color del texto en formato RGB.
        :param font: Tipo de fuente utilizada.
        :param size: Tamaño de la fuente.
        """
        self._points = points
        self._text_color = text_color
        self._font = font
        self._size = size

    def draw(self) -> None:
        """
        Muestra la puntuación actual en pantalla.
        """
        print(f"Score: {self._points}")


    # Métodos de acceso para obtener atributos encapsulados.
    @property
    def points(self) -> int:
        return self._points

    @property
    def text_color(self) -> tuple[int,int,int]:
        return self._text_color

    @property
    def font(self) -> str:
        return self._font

    @property
    def size(self) -> float:
        return self._size

    # Métodos modificadores (setter) para cambiar valores de los atributos encapsulados.
    @points.setter
    def points(self, points : int) -> None:
        self._points = points

    @text_color.setter
    def text_color(self, text_color: tuple[int,int,int]) -> None:
        self._text_color = text_color

    @font.setter
    def font(self, font: str) -> None:
        self._font = font

    @size.setter
    def size(self, size: float) -> None:
        self._size = size

    def __str__(self) -> str:
        """
        Retorna una representación en cadena del objeto Scoreboard.
        """
        return f"Scoreboard ( points = {self._points},  text_color = ({self._text_color}), font = {self._font}, size = {self._size})"

def main() -> None:
    """
    Función principal.
    """
    # Se crean objetos de la clase y se imprime.
    print("  -- Se crean objetos de la clase Scoreboard.")

    print()
    print("Se crea un objeto sin argumentos:")
    marcador1 = Scoreboard()
    print(f"marcador1 = {marcador1}")

    print()
    print("Se crea otro objeto con (points, font y text_color) como argumentos por nombre:")
    marcador2 = Scoreboard(10, font = "Arial", text_color = (127, 127, 127))
    print(f"marcador2 = {marcador2}")


    print()
    print("Se prueba el método draw() en ambos objetos:")
    marcador1.draw()
    marcador2.draw()


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()

