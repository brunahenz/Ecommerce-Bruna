
import pytest

from ecommerce.estrategia_rendimento import (
    EstrategiaRendimento,
    RendimentoBruto,
    RendimentoLiquido,
)


def test_rendimento_bruto():
    assert RendimentoBruto().calcular(1000, 10) == 100


def test_rendimento_liquido():
    estrategia = RendimentoLiquido(20)
    assert estrategia.calcular(1000, 10) == 80


def test_rendimento_liquido_sem_imposto():
    estrategia = RendimentoLiquido(0)
    assert estrategia.calcular(1000, 10) == 100


def test_rendimento_rejeita_valor_negativo():
    with pytest.raises(ValueError):
        RendimentoBruto().calcular(-1000, 10)


def test_rendimento_rejeita_taxa_negativa():
    with pytest.raises(ValueError):
        RendimentoBruto().calcular(1000, -1)


def test_imposto_invalido():
    with pytest.raises(ValueError):
        RendimentoLiquido(101)


def test_estrategia_rendimento_e_abstrata():
    with pytest.raises(TypeError):
        EstrategiaRendimento()
