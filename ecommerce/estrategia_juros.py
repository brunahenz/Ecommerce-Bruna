
from abc import ABC, abstractmethod


class EstrategiaJuros(ABC):
    @abstractmethod
    def calcular(
        self,
        valor: float,
        taxa: float,
        periodos: int,
    ) -> float:
        pass


class JurosSimples(EstrategiaJuros):
    def calcular(
        self,
        valor: float,
        taxa: float,
        periodos: int,
    ) -> float:
        self._validar(valor, taxa, periodos)
        return valor * (1 + taxa / 100 * periodos)

    @staticmethod
    def _validar(valor: float, taxa: float, periodos: int) -> None:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        if taxa < 0:
            raise ValueError("A taxa não pode ser negativa.")
        if not isinstance(periodos, int) or isinstance(periodos, bool):
            raise TypeError("Os períodos devem ser um número inteiro.")
        if periodos < 0:
            raise ValueError("Os períodos não podem ser negativos.")


class JurosCompostos(EstrategiaJuros):
    def calcular(
        self,
        valor: float,
        taxa: float,
        periodos: int,
    ) -> float:
        JurosSimples._validar(valor, taxa, periodos)
        return valor * (1 + taxa / 100) ** periodos
