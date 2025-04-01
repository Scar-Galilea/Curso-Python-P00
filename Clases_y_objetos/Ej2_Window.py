"""
Nombre: Galilea Peralta Contreras.
Fecha: 24 de marzo del 2025.

Descripción:
Se necesita desarrollar un sistema que permita gestionar y visualizar un scoreboard (puntuación) dentro de una ventana gráfica. El sistema debe cumplir con los siguientes requisitos:


2. Ventana:

Debe contener un scoreboard como parte de su interfaz.
Debe permitir actualizar el puntaje del scoreboard.
Debe ser capaz de redibujar el scoreboard cuando se actualice la puntuación.
3. Encapsulamiento:

La lógica del scoreboard debe estar encapsulada en una clase independiente.
La ventana debe interactuar con el scoreboard a través de una relación de agregación.
4. Flexibilidad:


El sistema debe ser fácil de extender, por ejemplo, para agregar más elementos gráficos o funcionalidades adicionales.

"""
from Ej2_Scoreboard import Scoreboard

class Window:
    def __init__(self, title: str, width: int, height: int, scoreboard: Scoreboard = Scoreboard()):
        self._title = title
        self._width = width
        self._height = height
        self._scoreboard = scoreboard

    def draw_scoreboard(self) -> None:
        self._scoreboard.draw()

    def update_score(self,points: int) -> None:
        self._scoreboard.points = points
        self._scoreboard.draw()

    @property
    def title(self) -> str:
        return self._title

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def scoreboard(self) -> Scoreboard():
        return self._scoreboard

    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    @width.setter
    def width(self, width: int) -> None:
        self._width= width

    @height.setter
    def height(self, height: int) -> None:
        self._height = height

    @scoreboard.setter
    def scoreboard(self, scoreboard: Scoreboard = Scoreboard()) -> None:
        self._scoreboard = scoreboard

    def __str__(self) -> str:
        return f"Window ( title = {self._title}, width = {self._width}, height = {self._height}, scoreboard = {self.scoreboard})"


def main() -> None:
    """
    Función principal.
    """
    # Se crean objetos de la clase Window sin un objeto de la clase Scoreboard creado
    # y se prueban sus métodos.
    print("  -- Se crea un objeto de la clase Window sin un objeto de la clase Scoreboard.")

    buscaminas = Window("Buscaminas", 800, 900)

    print("Se imprime el objeto:")
    print(f"Buscaminas = {buscaminas}")

    print()
    print("Método para dibujar el scoreboard:")
    buscaminas.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    buscaminas.update_score(1)

    # Se crean objetos de ambas clases y se prueban sus métodos.
    print()
    print("  -- Se crea otro objeto de la clase Window, pero ahora con un objeto de la clase Scoreboard.")

    marcador_solitario = Scoreboard(10, (40, 40, 40), "Arial", 40)
    solitario = Window("Solitario", 1_000, 1_000, marcador_solitario)

    print("Se imprimen los objetos:")
    print(f"marcador_solitario = {marcador_solitario}")
    print(f"Solitario = {solitario}")

    print()
    print("Método para dibujar el scoreboard:")
    solitario.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    solitario.update_score(11)

    # Se modifican los atributos mediante los métodos de acceso.
    print()
    print("  -- Se modifican los atributos mediante los métodos de acceso.")

    print("Se tiene la ventana buscaminas:")
    print(f"buscaminas = {buscaminas}")
    print("Se reemplaza el scoreboard utilizando el setter:")
    buscaminas.scoreboard = marcador_solitario
    print(f"buscaminas = {buscaminas}")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
