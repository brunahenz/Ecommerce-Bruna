
import pytest

from ecommerce.despesa import Despesa
from ecommerce.importador import (
    CriadorImportador,
    ImportadorBancoA,
    ImportadorBancoB,
)
from ecommerce.receita import Receita


def test_fabrica_cria_importador_banco_a():
    assert isinstance(
        CriadorImportador.criar("banco_a"),
        ImportadorBancoA,
    )


def test_fabrica_cria_importador_banco_b():
    assert isinstance(
        CriadorImportador.criar("banco_b"),
        ImportadorBancoB,
    )


def test_fabrica_rejeita_banco_desconhecido():
    with pytest.raises(ValueError, match="Banco não suportado"):
        CriadorImportador.criar("banco_c")


def test_importador_banco_a_cria_receita_e_despesa():
    importador = ImportadorBancoA()

    lancamentos = importador.importar([
        {
            "descricao": "Salário",
            "valor": 2500,
            "tipo": "receita",
            "categoria": "Renda",
        },
        {
            "descricao": "Mercado",
            "valor": 150,
            "tipo": "despesa",
            "categoria": "Alimentação",
        },
    ])

    assert len(lancamentos) == 2
    assert isinstance(lancamentos[0], Receita)
    assert isinstance(lancamentos[1], Despesa)


def test_importador_banco_b_interpreta_campos_diferentes():
    importador = ImportadorBancoB()

    lancamentos = importador.importar([
        {
            "historico": "Conta de luz",
            "valor_movimentacao": 120,
            "operacao": "despesa",
            "grupo": "Moradia",
        },
    ])

    assert len(lancamentos) == 1
    assert isinstance(lancamentos[0], Despesa)
    assert lancamentos[0].descricao == "Conta de luz"
    assert lancamentos[0].categoria.nome == "Moradia"


def test_importador_rejeita_tipo_invalido():
    importador = ImportadorBancoA()

    with pytest.raises(ValueError, match="Tipo de lançamento inválido"):
        importador.importar([
            {
                "descricao": "Movimentação",
                "valor": 50,
                "tipo": "desconhecido",
                "categoria": "Outros",
            },
        ])
