
from ecommerce.receita import Receita
from ecommerce.despesa import Despesa


class Extrato:

    def __init__(self, lancamentos=None) -> None:
        self.lancamentos = lancamentos if lancamentos is not None else []

    def quantidade_lancamentos(self) -> int:
        return len(self.lancamentos)

    def gerar_linhas(self) -> list[str]:
        linhas = []

        for lancamento in self.lancamentos:
            if isinstance(lancamento, Receita):
                sinal = "+"
            elif isinstance(lancamento, Despesa):
                sinal = "-"
            else:
                continue

            linhas.append(
                f"{lancamento.descricao}: {sinal}R$ {lancamento.valor:.2f}"
            )

        return linhas
