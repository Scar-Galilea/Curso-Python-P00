"""
Nombre: Galilea Peralta Contreras.
Fecha: 11 de marzo del 2025.

Descripción:

"""

class CuentaBancaria:
    contador_id = 1
    def __init__(self, titular: str, saldo_inicial: float = 0)-> None:

        self.titular = titular
        self._saldo_inicial = saldo_inicial
        self.contador_id  = CuentaBancaria.contador_id
        CuentaBancaria.contador_id += 1
    def depositar(self,cantidad :float) -> None:
        pass
    def retirar(self,cantidad :float) -> None:
        pass
    @property
    def saldo(self)-> float:
        return self.saldo
    @ saldo.setter
    def saldo(self) -> float:
        return self.saldo
    def __str__(self) -> str:
        return f"Cuenta Bancaria  ( id = {self.contador_id}, titular: {self.titular}, saldo inicial: {self.saldo_inicial}.)"


def main() -> None:
    """
    Función principal.
    """
    cuenta_guadalupe = (CuentaBancaria("Guadalupe",0))
    cuenta_guadalupe.saldo = 5



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()

