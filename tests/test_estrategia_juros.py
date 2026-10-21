
import pytest

from ecommerce.estrategia_juros import (
    EstrategiaJuros,
    JurosCompostos,
    JurosSimples,
)


def test_juros_simples():
    assert JurosSimples().calcular(1000, 10, 2) == 1200


def test_juros_compostos():
    assert JurosCompostos().calcular(1000, 10, 2) == pytest.approx(1210)


def test_juros_simples_sem_periodos():
    assert JurosSimples().calcular(1000, 10, 0) == 1000


def test_juros_compostos_sem_periodos():
    assert JurosCompostos().calcular(1000, 10, 0) == 1000


def test_valor_negativo():
    with pytest.raises(ValueError):
        JurosSimples().calcular(-1000, 10, 2)


def test_taxa_negativa():
    with pytest.raises(ValueError):
        JurosCompostos().calcular(1000, -1, 2)


def test_periodos_negativos():
    with pytest.raises(ValueError):
        JurosSimples().calcular(1000, 10, -2)


def test_periodos_nao_inteiros():
    with pytest.raises(TypeError):
        JurosCompostos().calcular(1000, 10, 2.5)


def test_estrategia_juros_e_abstrata():
    with pytest.raises(TypeError):
        EstrategiaJuros()
