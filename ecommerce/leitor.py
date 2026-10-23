
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
import csv
import json

from ecommerce.categoria import Categoria
from ecommerce.despesa import Despesa
from ecommerce.receita import Receita


class Leitor(ABC):
    """Define como ler os dados de um arquivo."""

    @abstractmethod
    def ler_registros(self, caminho: str) -> list[dict]:
        pass

    def ler(self, caminho: str) -> list:
        return self._criar_lancamentos(self.ler_registros(caminho))

    def _criar_lancamentos(self, registros: list[dict]) -> list:
        lancamentos = []

        for registro in registros:
            descricao = registro.get("descricao")
            valor = registro.get("valor")
            tipo = str(registro.get("tipo", "")).strip().lower()
            nome_categoria = registro.get("categoria")
            data_texto = registro.get("data")

            if not nome_categoria or not str(nome_categoria).strip():
                raise ValueError(
                    "Todo lançamento precisa ter uma categoria."
                )

            categoria = Categoria(str(nome_categoria))
            data = (
                datetime.fromisoformat(data_texto)
                if data_texto
                else None
            )

            if tipo == "receita":
                lancamento = Receita(
                    descricao, valor, categoria, data
                )
            elif tipo == "despesa":
                lancamento = Despesa(
                    descricao, valor, categoria, data
                )
            else:
                raise ValueError(
                    f"Tipo de lançamento inválido: {tipo}"
                )

            lancamentos.append(lancamento)

        return lancamentos


class LeitorCSV(Leitor):
    def ler_registros(self, caminho: str) -> list[dict]:
        with open(
            caminho, "r", encoding="utf-8-sig", newline=""
        ) as arquivo:
            return list(csv.DictReader(arquivo))


class LeitorJSON(Leitor):
    def ler_registros(self, caminho: str) -> list[dict]:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            registros = json.load(arquivo)

        if not isinstance(registros, list):
            raise ValueError(
                "O arquivo JSON deve conter uma lista de lançamentos."
            )

        if not all(isinstance(registro, dict) for registro in registros):
            raise ValueError(
                "Cada lançamento do JSON deve ser um objeto."
            )

        return registros


class CriadorLeitor:
    """Escolhe o leitor pela extensão do arquivo."""

    @staticmethod
    def criar(caminho: str) -> Leitor:
        extensao = Path(caminho).suffix.lower()

        if extensao == ".csv":
            return LeitorCSV()
        if extensao == ".json":
            return LeitorJSON()

        raise ValueError(
            f"Formato de arquivo não suportado: "
            f"{extensao or 'sem extensão'}"
        )
