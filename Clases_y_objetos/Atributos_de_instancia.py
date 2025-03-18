"""
Nombre: Galilea Peralta Contreras.
Fecha: 05 de marzo del 2025.

Descripción:

"""

class Estudiante:
    def __init__(self, nombre: str):
        # Asignar la variable como un objeto.
        self.nombre = nombre
        self.temas_aprendidos = []

    def aprender_temas(self,tema:str) -> None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")

    def __str__(self) -> str:
        return f"Estudiante  (nombre: {self.nombre}. Temas aprendidos: {self.temas_aprendidos})"

class Profesor:
    def __init__(self,nombre: str, temas_dominados: list[str]):
        self.nombre = nombre
        self.temas_dominados = temas_dominados

    def dominar_tema(self,tema:str) -> None:
        self.temas_dominados.append(tema)
        print(f"{self.nombre} dominó {tema}")

    def ensenar_tema(self, no_tema: int) -> str :
        if no_tema < len(self.temas_dominados):
            return self.temas_dominados[no_tema]
        else:
            return "Fuera de rango"


    def __str__(self) -> str:
        return f"Profesor  (nombre: {self.nombre}. Temas dominados: {self.temas_dominados})"



def main() -> None:
    """
    Función principal.
    """


    scarlett = Estudiante("Scarlett")
    galilea = Estudiante("Galilea")


    alberto = Profesor("Alberto",["Diseño web","Español"])
    a = alberto.ensenar_tema(1)

    scarlett.aprender_temas(alberto.ensenar_tema(1))
    galilea.aprender_temas(alberto.ensenar_tema(1))


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
