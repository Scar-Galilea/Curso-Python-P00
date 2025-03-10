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

    def ensenar_tema(self, no_tema: int) -> str | None:
        if no_tema > len(self.temas_dominados):
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
    print()
    scarlett.aprender_temas("Evolución de los stiios web")
    galilea.aprender_temas("Internet de la cosas")
    print()
    print(scarlett)
    print(galilea)
    print()
    alberto = Profesor("Alberto",["Diseño web","Español"])
    alberto.ensenar_tema(2)
    print(alberto)


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
