
from ecommerce.lancamento import Lancamento
from ecommerce.receita import Receita
from ecommerce.despesa import Despesa


class Fechamento:

    def __init__(self, lancamentos: list[Lancamento] = None) -> None:
        self.lancamentos = lancamentos if lancamentos is not None else []

    def total_receitas(self) -> float:
        return sum(
            l.valor
            for l in self.lancamentos
            if isinstance(l, Receita)
        )

    def total_despesas(self) -> float:
        return sum(
            l.valor
            for l in self.lancamentos
            if isinstance(l, Despesa)
        )

    def saldo_final(self) -> float:
        return self.total_receitas() - self.total_despesas()
