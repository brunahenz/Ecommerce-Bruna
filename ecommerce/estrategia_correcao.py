
from abc import ABC, abstractmethod


class EstrategiaCorrecao(ABC):
    @abstractmethod
    def calcular(self, valor: float, taxa: float) -> float:
        pass


class SemCorrecao(EstrategiaCorrecao):
    def calcular(self, valor: float, taxa: float = 0) -> float:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        return valor


class CorrecaoPercentual(EstrategiaCorrecao):
    def calcular(self, valor: float, taxa: float) -> float:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        if taxa < 0:
            raise ValueError("A taxa de correção não pode ser negativa.")

        return valor * (1 + taxa / 100)
