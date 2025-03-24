"""
Nombre: Galilea Peralta Contreras.
Fecha: 11 de marzo del 2025.

Descripción:

"""

class Scoreboard:
    def __init__(self,points : int = 0,text_color: tuple[int,int,int] = (0,0,0),font: str = 'Kimono',size: float = 48):
        self.points = points
        self.text_color = text_color
        self.font = font
        self.size = size
        self.x = 0
        self.y = 0

    def draw(self) -> None:
        print(f"Score: {self.points}")

    @property
    def points(self) -> int:
        return self.points

    @property
    def text_color(self) -> tuple[int]:
        return self.text_color

    @property
    def font(self) -> float:
        return self.font

    @property
    def size(self) -> str:
        return self.size

    @points.setter
    def points(self, value):
        self._points = value

    @text_color.setter
    def text_color(self, value):
        self._text_color = value

    @font.setter
    def font(self, value):
        self._font = value

    @size.setter
    def size(self, value):
        self._size = value

    def __str__(self) -> str:
        pass
        #return f"Empleado  ( Id = {self.no_id}. Nombre: {self.nombre}. Sueldo: {self.sueldo})"

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

