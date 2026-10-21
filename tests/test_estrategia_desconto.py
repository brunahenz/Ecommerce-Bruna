
import pytest

from ecommerce.estrategia_desconto import (
    DescontoFixo,
    DescontoPercentual,
    EstrategiaDesconto,
)


def test_desconto_percentual():
    estrategia = DescontoPercentual(10)
    assert estrategia.calcular(200) == 180


def test_desconto_fixo():
    estrategia = DescontoFixo(30)
    assert estrategia.calcular(200) == 170


def test_desconto_fixo_nao_deixa_valor_negativo():
    estrategia = DescontoFixo(300)
    assert estrategia.calcular(200) == 0


def test_percentual_invalido():
    with pytest.raises(ValueError):
        DescontoPercentual(101)


def test_desconto_fixo_negativo():
    with pytest.raises(ValueError):
        DescontoFixo(-10)


def test_valor_negativo():
    estrategia = DescontoPercentual(10)

    with pytest.raises(ValueError):
        estrategia.calcular(-100)


def test_estrategia_desconto_e_abstrata():
    with pytest.raises(TypeError):
        EstrategiaDesconto()
