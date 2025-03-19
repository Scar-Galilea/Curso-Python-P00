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
        return f"Empleado ( Id = {self.no_id}. Nombre: {self.nombre}. Sueldo: {self.sueldo})"

class Empresa:
    def __init__(self, nombre: str , *empleados: Empleado ):
        # Asignar la variable como un objeto.
        self.nombre = nombre
        self.empleados = list(empleados)

    def agregar_empleados(self,*nuevos_empleados:Empleado):
        for empleado in list(nuevos_empleados):
            self.empleados.append(empleado)

    def __str__(self) -> str:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        # Se convierte los elementos de la lista en cadenas (invocando str() para cada uno de ellos) y
        # se unen con ", " a través del métod0 str.join().
        # Este patrón es muy común en Python para obtener una cadena a partir de una lista.
        empleados = ", ".join(str(empleado) for empleado in self.empleados)
        return f"Empresa :  Nombre: {self.nombre}, {empleados}"


def main() -> None:
    """
    Función principal.
    """

    # Se crean varios objetos de la clase Empleado y se imprimen en consola.
    alberto = Empleado("Alberto Martínez", 1110.1)
    gerardo = Empleado("Gerardo Guerrero", 12_123.23)

    emp = Empresa("Unsij",alberto,gerardo)
    print(emp)
    emp.agregar_empleados(Empleado("Scarlett",3000))
    print(emp)

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()

