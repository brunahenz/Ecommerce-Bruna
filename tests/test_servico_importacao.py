
import json

import pytest

from ecommerce.aplicacao import montar_aplicacao
from ecommerce.exportador_relatorio import ExportadorCSV
from ecommerce.servico_importacao import ServicoImportacao


class LeitorFalso:
    def ler_registros(self, caminho):
        return [{
            "descricao": "Salário",
            "valor": 2000,
            "tipo": "receita",
            "categoria": "Renda",
        }]


class CriadorLeitorFalso:
    @staticmethod
    def criar(caminho):
        return LeitorFalso()


class ImportadorFalso:
    def importar(self, registros):
        assert len(registros) == 1
        return []


class CriadorImportadorFalso:
    @staticmethod
    def criar(banco):
        assert banco == "banco_a"
        return ImportadorFalso()


class ExportadorFalso:
    def __init__(self):
        self.foi_chamado = False
        self.lancamentos_recebidos = None
        self.caminho_recebido = None

    def exportar(self, lancamentos, caminho):
        self.foi_chamado = True
        self.lancamentos_recebidos = lancamentos
        self.caminho_recebido = caminho


def test_servico_usa_dependencias_injetadas():
    exportador = ExportadorFalso()

    servico = ServicoImportacao(
        CriadorLeitorFalso,
        CriadorImportadorFalso,
        exportador,
    )

    resultado = servico.executar(
        "entrada.csv",
        "banco_a",
        "saida.csv",
    )

    assert resultado == []
    assert exportador.foi_chamado
    assert exportador.lancamentos_recebidos == []
    assert exportador.caminho_recebido == "saida.csv"


def test_composicao_raiz_cria_servico_com_exportador_csv():
    servico = montar_aplicacao("csv")

    assert isinstance(servico, ServicoImportacao)
    assert isinstance(servico.exportador, ExportadorCSV)


def test_servico_importa_arquivo_e_gera_relatorio_csv(tmp_path):
    entrada = tmp_path / "banco.csv"
    saida = tmp_path / "relatorio.csv"

    entrada.write_text(
        "descricao,valor,tipo,categoria\n"
        "Salário,2000,receita,Renda\n"
        "Mercado,300,despesa,Alimentação\n",
        encoding="utf-8",
    )

    servico = montar_aplicacao("csv")
    resultado = servico.executar(
        str(entrada),
        "banco_a",
        str(saida),
    )

    conteudo = saida.read_text(encoding="utf-8")

    assert len(resultado) == 2
    assert "total_receitas;2000.00" in conteudo
    assert "total_despesas;300.00" in conteudo
    assert "saldo_final;1700.00" in conteudo


def test_composicao_raiz_rejeita_formato_desconhecido():
    with pytest.raises(ValueError, match="não suportado"):
        montar_aplicacao("pdf")
