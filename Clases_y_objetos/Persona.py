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
        self.peso = nombre
        # S e construyo a una persona

    # Mis metodos:
    def caminar(self) -> None:
        print("Estoy caminando.")

    def comer(self) -> None:
        print("Estoy comiendo.")

    def jugar(self) -> None:
        print("Estoy jugando.")

    def dormir(self) -> None:
        print("Estoy durmiendo.")

def main() -> None:
    """
    Función principal.
    """
    # Las clases siempre van en mayuscula.

    galilea = Persona("Galilea",19,1.60,56)

    print(galilea.nombre)
    galilea.caminar()

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
