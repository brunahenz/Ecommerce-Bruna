
from abc import ABC, abstractmethod


class EstrategiaTaxa(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass


class SemTaxa(EstrategiaTaxa):
    def calcular(self, valor: float) -> float:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        return 0.0


class TaxaFixa(EstrategiaTaxa):
    def __init__(self, taxa: float):
        if taxa < 0:
            raise ValueError("A taxa não pode ser negativa.")
        self.__taxa = taxa

    def calcular(self, valor: float) -> float:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        return self.__taxa


class TaxaPercentual(EstrategiaTaxa):
    def __init__(self, percentual: float):
        if not 0 <= percentual <= 100:
            raise ValueError("O percentual deve estar entre 0 e 100.")
        self.__percentual = percentual

    def calcular(self, valor: float) -> float:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        return valor * self.__percentual / 100
