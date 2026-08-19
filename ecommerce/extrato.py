class Extrato:

    def __init__(self, lancamentos=None) -> None:
        self.lancamentos = lancamentos if lancamentos is not None else []

    def quantidade_lancamentos(self) -> int:
        return len(self.lancamentos)

    def gerar_linhas(self) -> list[str]:
        linhas = []
        for l in self.lancamentos:
            sinal = "+" if l.tipo == "receita" else "-"
            linhas.append(f"{l.descricao}: {sinal}R$ {l.valor:.2f}")
        return linhas