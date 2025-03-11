"""
Nombre: Galilea Peralta Contreras.
Fecha: 11 de marzo del 2025.

Descripción:

"""

class Empleado:
    no_id = 1
    def __init__(self, nombre: str , sueldo: float):
        # Asignar la variable como un objeto.
        self.nombre = nombre
        self.sueldo = sueldo
        self.no_id  = Empleado.no_id
        Empleado.no_id += 1

    def aumentar_sueldo(self,porcentaje : float) -> None:
        pass

    def __str__(self) -> str:
        return f"Empleado  ( Id = {self.no_id}. Nombre: {self.nombre}. Sueldo: {self.sueldo})"


def main() -> None:
    """
    Función principal.
    """
    print(Empleado.no_id)
    Empleado_1 = Empleado('Sofia',1500)
    Empleado_2 = Empleado('Ana', 2000)

    print(Empleado_1)
    print(Empleado_2)

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()

