
import json

import pytest

from ecommerce.despesa import Despesa
from ecommerce.leitor import CriadorLeitor, LeitorCSV, LeitorJSON
from ecommerce.receita import Receita


def test_criador_escolhe_leitor_csv():
    assert isinstance(
        CriadorLeitor.criar("lancamentos.csv"), LeitorCSV
    )


def test_criador_escolhe_leitor_json():
    assert isinstance(
        CriadorLeitor.criar("lancamentos.json"), LeitorJSON
    )


def test_criador_rejeita_formato_nao_suportado():
    with pytest.raises(ValueError, match="não suportado"):
        CriadorLeitor.criar("lancamentos.xlsx")


def test_leitor_csv_cria_receita_e_despesa(tmp_path):
    arquivo = tmp_path / "lancamentos.csv"
    arquivo.write_text(
        "descricao,valor,tipo,categoria,data\n"
        "Salário,2500,receita,Renda,2026-10-01T10:00:00\n"
        "Mercado,120,despesa,Alimentação,2026-10-02T12:00:00\n",
        encoding="utf-8",
    )

    lancamentos = LeitorCSV().ler(str(arquivo))

    assert len(lancamentos) == 2
    assert isinstance(lancamentos[0], Receita)
    assert isinstance(lancamentos[1], Despesa)
    assert lancamentos[0].valor == 2500
    assert lancamentos[1].categoria.nome == "Alimentação"


def test_leitor_json_cria_lancamento(tmp_path):
    arquivo = tmp_path / "lancamentos.json"
    arquivo.write_text(
        json.dumps([{
            "descricao": "Freelance",
            "valor": 500,
            "tipo": "receita",
            "categoria": "Trabalho",
            "data": "2026-10-03T09:00:00",
        }]),
        encoding="utf-8",
    )

    lancamentos = LeitorJSON().ler(str(arquivo))

    assert len(lancamentos) == 1
    assert isinstance(lancamentos[0], Receita)
    assert lancamentos[0].descricao == "Freelance"


def test_leitor_json_rejeita_conteudo_que_nao_seja_lista(tmp_path):
    arquivo = tmp_path / "lancamentos.json"
    arquivo.write_text(
        '{"descricao": "Salário"}', encoding="utf-8"
    )

    with pytest.raises(ValueError, match="deve conter uma lista"):
        LeitorJSON().ler(str(arquivo))


def test_leitor_rejeita_tipo_invalido(tmp_path):
    arquivo = tmp_path / "lancamentos.csv"
    arquivo.write_text(
        "descricao,valor,tipo,categoria\n"
        "Transferência,20,transferencia,Outros\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Tipo de lançamento inválido"):
        LeitorCSV().ler(str(arquivo))
