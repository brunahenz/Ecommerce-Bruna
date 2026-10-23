
from abc import ABC, abstractmethod

from ecommerce.fechamento import Fechamento
from ecommerce.extrato import Extrato


class ExportadorRelatorio(ABC):
    """Define o fluxo de geração e exportação de relatórios."""

    def exportar(self, lancamentos: list, caminho: str) -> None:
        fechamento = Fechamento(lancamentos)
        extrato = Extrato(lancamentos)

        relatorio = {
            "quantidade_lancamentos": extrato.quantidade_lancamentos(),
            "total_receitas": fechamento.total_receitas(),
            "total_despesas": fechamento.total_despesas(),
            "saldo_final": fechamento.saldo_final(),
            "lancamentos": extrato.gerar_linhas(),
        }

        conteudo = self.criar_documento(relatorio)

        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)

    @abstractmethod
    def criar_documento(self, relatorio: dict) -> str:
        """Cria o documento no formato escolhido."""
        pass


class ExportadorCSV(ExportadorRelatorio):
    def criar_documento(self, relatorio: dict) -> str:
        linhas = [
            "indicador;valor",
            f"quantidade_lancamentos;{relatorio['quantidade_lancamentos']}",
            f"total_receitas;{relatorio['total_receitas']:.2f}",
            f"total_despesas;{relatorio['total_despesas']:.2f}",
            f"saldo_final;{relatorio['saldo_final']:.2f}",
            "",
            "lancamentos",
        ]

        linhas.extend(relatorio["lancamentos"])
        return "\n".join(linhas)


class ExportadorHTML(ExportadorRelatorio):
    def criar_documento(self, relatorio: dict) -> str:
        linhas = "".join(
            f"<li>{linha}</li>"
            for linha in relatorio["lancamentos"]
        )

        return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Relatório financeiro</title>
</head>
<body>
    <h1>Relatório financeiro</h1>
    <p>Quantidade de lançamentos:
       {relatorio['quantidade_lancamentos']}</p>
    <p>Total de receitas: R$ {relatorio['total_receitas']:.2f}</p>
    <p>Total de despesas: R$ {relatorio['total_despesas']:.2f}</p>
    <p>Saldo final: R$ {relatorio['saldo_final']:.2f}</p>
    <h2>Lançamentos</h2>
    <ul>{linhas}</ul>
</body>
</html>"""
