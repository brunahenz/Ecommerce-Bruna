
from datetime import date

from ecommerce.estrategia_desconto import EstrategiaDesconto


class Cupom:
    def __init__(
        self,
        codigo: str,
        validade: date,
        estrategia_desconto: EstrategiaDesconto,
    ):
        if not codigo or not codigo.strip():
            raise ValueError("O código do cupom não pode ser vazio.")

        if not isinstance(validade, date):
            raise TypeError("A validade deve ser uma data.")

        if not isinstance(estrategia_desconto, EstrategiaDesconto):
            raise TypeError("A estratégia de desconto é inválida.")

        self.__codigo = codigo.strip().upper()
        self.__validade = validade
        self.__estrategia_desconto = estrategia_desconto

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def validade(self) -> date:
        return self.__validade

    def esta_valido(self, data_atual: date | None = None) -> bool:
        if data_atual is None:
            data_atual = date.today()

        return data_atual <= self.__validade

    def aplicar_desconto(
        self,
        valor: float,
        data_atual: date | None = None,
    ) -> float:
        if not self.esta_valido(data_atual):
            raise ValueError("O cupom está vencido.")

        return self.__estrategia_desconto.calcular(valor)
