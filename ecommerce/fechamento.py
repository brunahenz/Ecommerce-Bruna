from ecommerce.lancamento import Lancamento


class Fechamento:

    def __init__(self, lancamentos: list[Lancamento] = None) -> None:
        self.lancamentos = lancamentos if lancamentos is not None else []

    def total_receitas(self) -> float:
        return sum(l.valor for l in self.lancamentos if l.tipo == "receita")

    def total_despesas(self) -> float:
        return sum(l.valor for l in self.lancamentos if l.tipo == "despesa")

    def saldo_final(self) -> float:
        return self.total_receitas() - self.total_despesas()