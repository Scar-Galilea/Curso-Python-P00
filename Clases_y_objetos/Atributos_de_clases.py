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
        """
        Se utiliza para aumentar el sueldo de acuerdo con un porcentaje.
        :param porcentaje: Porcentaje a incrementar el sueldo.
        """
        if porcentaje > 0:
            self.sueldo += self.sueldo * (porcentaje / 100)
            print(f"El sueldo de {self.nombre} ahora es de {self.sueldo:,.2f}")

        else:
            print("No se aplicó ningún cambio, ya que por Ley, el sueldo no puede disminuir.")


    def __str__(self) -> str:
        return f"Empleado  ( Id = {self.no_id}. Nombre: {self.nombre}. Sueldo: {self.sueldo})"


def main() -> None:
    """
    Función principal.
    """
    print("  -- Ejemplo de uso de los atributos de clase.")

    # Forma de acceder al atributo de clase.
    print(f"Atributo de clase: {Empleado.no_id = }")

    # Se crean varios objetos de la clase Empleado y se imprimen en consola.
    alberto = Empleado("Alberto Martínez", 1110.1)
    gerardo = Empleado("Gerardo Guerrero", 12_123.23)
    esteban = Empleado("Esteban Ramírez", 999.23)

    print()
    print("Se crean empleados:")
    print(alberto)
    print(gerardo)
    print(esteban)

    # Se muestra nuevamente el atributo de clase.
    print()
    print(f"Atributo de clase: {Empleado.no_id = }")
    alberto.aumentar_sueldo(4)

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()

