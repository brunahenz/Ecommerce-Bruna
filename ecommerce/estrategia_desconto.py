
from abc import ABC, abstractmethod


class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass


class DescontoPercentual(EstrategiaDesconto):
    def __init__(self, percentual: float):
        if not 0 <= percentual <= 100:
            raise ValueError("O percentual deve estar entre 0 e 100.")
        self.__percentual = percentual

    def calcular(self, valor: float) -> float:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        return valor * (1 - self.__percentual / 100)


class DescontoFixo(EstrategiaDesconto):
    def __init__(self, desconto: float):
        if desconto < 0:
            raise ValueError("O desconto não pode ser negativo.")
        self.__desconto = desconto

    def calcular(self, valor: float) -> float:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        return max(0.0, valor - self.__desconto)
