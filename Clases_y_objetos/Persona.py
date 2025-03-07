"""
Nombre: Galilea Peralta Contreras.
Fecha: 05 de marzo del 2025.

Descripción:

"""

class Persona:
    # El self se refiere a uno mismo, en este caso al objeto que estamos costruyendo.
    def __init__(self, nombre: str, edad: int, altura: float, peso: float):
        # Asignar la variable como un objeto.
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        # S e construyo a una persona

    # Mis metodos:
    def caminar(self) -> None:
        print(f"{self.nombre} está caminando para bajar sus {self.peso} kgs.")

    def comer(self) -> None:
        print(f"{self.nombre} está comiendo un pastel por su cumpleaños número {self.edad} años.")

    def jugar(self) -> None:
        print(f"{self.nombre} está jugando Mobile legends bang bang.")

    def dormir(self) -> None:
        print(f"{self.nombre} está durmiendo temprano para madrugar.")

def main() -> None:
    """
    Función principal.
    """
    # Las clases siempre van en mayuscula.

    galilea = Persona("Galilea",19,1.60,56)

    print(galilea.nombre)
    galilea.caminar()

    print()
    rosalinda = Persona("Rosalinda",21,1.50,56)
    rosalinda.caminar()
    rosalinda.comer()
    rosalinda.jugar()
    rosalinda.dormir()

    print()
    galilea.peso = 55
    galilea.altura = 1.61

    print(galilea.peso,galilea.altura)
    galilea.caminar()

    print()
    print(galilea.nombre)

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
