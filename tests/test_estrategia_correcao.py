
import pytest

from ecommerce.estrategia_correcao import (
    CorrecaoPercentual,
    EstrategiaCorrecao,
    SemCorrecao,
)


def test_sem_correcao():
    assert SemCorrecao().calcular(1000) == 1000


def test_correcao_percentual():
    assert CorrecaoPercentual().calcular(1000, 5) == 1050


def test_correcao_com_taxa_zero():
    assert CorrecaoPercentual().calcular(1000, 0) == 1000


def test_correcao_rejeita_valor_negativo():
    with pytest.raises(ValueError):
        CorrecaoPercentual().calcular(-1000, 5)


def test_correcao_rejeita_taxa_negativa():
    with pytest.raises(ValueError):
        CorrecaoPercentual().calcular(1000, -5)


def test_sem_correcao_rejeita_valor_negativo():
    with pytest.raises(ValueError):
        SemCorrecao().calcular(-1000)


def test_estrategia_correcao_e_abstrata():
    with pytest.raises(TypeError):
        EstrategiaCorrecao()
