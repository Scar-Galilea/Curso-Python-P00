"""
Nombre: Galilea Peralta Contreras.
Fecha: 11 de marzo del 2025.

Descripción:

"""

class Scoreboard:
    def __init__(self,points : int = 0,text_color: tuple[int,int,int] = (0,0,0),font: str = 'Kimono',size: float = 48):
        self._points = points
        self._text_color = text_color
        self._font = font
        self._size = size

    def draw(self) -> None:
        print(f"Score: {self._points}")

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

