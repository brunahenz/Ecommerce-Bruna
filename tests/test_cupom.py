
from datetime import date, timedelta

import pytest

from ecommerce.cupom import Cupom
from ecommerce.estrategia_desconto import DescontoPercentual


def test_criar_cupom():
    cupom = Cupom(
        " economia10 ",
        date.today() + timedelta(days=10),
        DescontoPercentual(10),
    )

    assert cupom.codigo == "ECONOMIA10"


def test_cupom_aplica_desconto():
    cupom = Cupom(
        "ECONOMIA10",
        date.today() + timedelta(days=10),
        DescontoPercentual(10),
    )

    assert cupom.aplicar_desconto(200) == 180


def test_cupom_vencido():
    cupom = Cupom(
        "VENCIDO",
        date.today() - timedelta(days=1),
        DescontoPercentual(10),
    )

    with pytest.raises(ValueError, match="vencido"):
        cupom.aplicar_desconto(200)


def test_cupom_vazio():
    with pytest.raises(ValueError):
        Cupom(
            " ",
            date.today(),
            DescontoPercentual(10),
        )


def test_cupom_rejeita_validade_invalida():
    with pytest.raises(TypeError):
        Cupom(
            "TESTE",
            "amanhã",
            DescontoPercentual(10),
        )


def test_cupom_rejeita_estrategia_invalida():
    with pytest.raises(TypeError):
        Cupom(
            "TESTE",
            date.today(),
            "10%",
        )


def test_cupom_valido_na_data_de_validade():
    hoje = date.today()
    cupom = Cupom(
        "HOJE",
        hoje,
        DescontoPercentual(10),
    )

    assert cupom.esta_valido(hoje)
