
from abc import ABC, abstractmethod

from ecommerce.categoria import Categoria
from ecommerce.despesa import Despesa
from ecommerce.receita import Receita


class Importador(ABC):
    """Interface para importação de lançamentos bancários."""

    @abstractmethod
    def importar(self, registros: list[dict]) -> list:
        pass

    def _criar_lancamento(
        self,
        descricao: str,
        valor: float,
        tipo: str,
        categoria: str,
    ):
        categoria_obj = Categoria(categoria)
        tipo = tipo.strip().lower()

        if tipo == "receita":
            return Receita(descricao, valor, categoria_obj)

        if tipo == "despesa":
            return Despesa(descricao, valor, categoria_obj)

        raise ValueError(f"Tipo de lançamento inválido: {tipo}")


class ImportadorBancoA(Importador):
    """Importa registros com os nomes de campos do Banco A."""

    def importar(self, registros: list[dict]) -> list:
        lancamentos = []

        for registro in registros:
            lancamentos.append(
                self._criar_lancamento(
                    registro["descricao"],
                    registro["valor"],
                    registro["tipo"],
                    registro["categoria"],
                )
            )

        return lancamentos


class ImportadorBancoB(Importador):
    """Importa registros com os nomes de campos do Banco B."""

    def importar(self, registros: list[dict]) -> list:
        lancamentos = []

        for registro in registros:
            lancamentos.append(
                self._criar_lancamento(
                    registro["historico"],
                    registro["valor_movimentacao"],
                    registro["operacao"],
                    registro["grupo"],
                )
            )

        return lancamentos


class CriadorImportador:
    """Escolhe o importador conforme o banco de origem."""

    @staticmethod
    def criar(banco: str) -> Importador:
        banco = banco.strip().lower()

        if banco == "banco_a":
            return ImportadorBancoA()

        if banco == "banco_b":
            return ImportadorBancoB()

        raise ValueError(f"Banco não suportado: {banco}")
