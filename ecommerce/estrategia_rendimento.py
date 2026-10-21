
from abc import ABC, abstractmethod


class EstrategiaRendimento(ABC):
    @abstractmethod
    def calcular(self, valor: float, taxa: float) -> float:
        pass

    @staticmethod
    def validar(valor: float, taxa: float) -> None:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        if taxa < 0:
            raise ValueError("A taxa não pode ser negativa.")


class RendimentoBruto(EstrategiaRendimento):
    def calcular(self, valor: float, taxa: float) -> float:
        self.validar(valor, taxa)
        return valor * taxa / 100


class RendimentoLiquido(EstrategiaRendimento):
    def __init__(self, imposto_percentual: float):
        if not 0 <= imposto_percentual <= 100:
            raise ValueError("O imposto deve estar entre 0 e 100.")
        self.__imposto_percentual = imposto_percentual

    def calcular(self, valor: float, taxa: float) -> float:
        self.validar(valor, taxa)
        rendimento_bruto = valor * taxa / 100
        imposto = rendimento_bruto * self.__imposto_percentual / 100
        return rendimento_bruto - imposto
