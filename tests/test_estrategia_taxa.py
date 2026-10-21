
import pytest

from ecommerce.estrategia_taxa import (
    EstrategiaTaxa,
    SemTaxa,
    TaxaFixa,
    TaxaPercentual,
)


def test_sem_taxa():
    assert SemTaxa().calcular(200) == 0


def test_taxa_fixa():
    assert TaxaFixa(5).calcular(200) == 5


def test_taxa_percentual():
    assert TaxaPercentual(2).calcular(200) == 4


def test_taxa_fixa_negativa():
    with pytest.raises(ValueError):
        TaxaFixa(-5)


def test_percentual_invalido():
    with pytest.raises(ValueError):
        TaxaPercentual(101)


def test_valor_negativo():
    with pytest.raises(ValueError):
        TaxaPercentual(2).calcular(-200)


def test_estrategia_taxa_e_abstrata():
    with pytest.raises(TypeError):
        EstrategiaTaxa()
