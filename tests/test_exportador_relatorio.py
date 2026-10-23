
import pytest

from ecommerce.categoria import Categoria
from ecommerce.receita import Receita
from ecommerce.despesa import Despesa
from ecommerce.exportador_relatorio import (
    ExportadorCSV,
    ExportadorHTML,
    ExportadorRelatorio,
)


@pytest.fixture
def lancamentos():
    categoria = Categoria("Geral")
    return [
        Receita("Salário", 2000, categoria),
        Despesa("Mercado", 300, categoria),
    ]


def test_exportador_csv_gera_relatorio(tmp_path, lancamentos):
    arquivo = tmp_path / "relatorio.csv"

    ExportadorCSV().exportar(lancamentos, str(arquivo))

    conteudo = arquivo.read_text(encoding="utf-8")

    assert "total_receitas;2000.00" in conteudo
    assert "total_despesas;300.00" in conteudo
    assert "saldo_final;1700.00" in conteudo
    assert "Salário" in conteudo
    assert "Mercado" in conteudo


def test_exportador_html_gera_relatorio(tmp_path, lancamentos):
    arquivo = tmp_path / "relatorio.html"

    ExportadorHTML().exportar(lancamentos, str(arquivo))

    conteudo = arquivo.read_text(encoding="utf-8")

    assert "<html" in conteudo
    assert "Relatório financeiro" in conteudo
    assert "R$ 2000.00" in conteudo
    assert "R$ 300.00" in conteudo
    assert "Salário" in conteudo


def test_exportadores_implementam_classe_abstrata():
    assert isinstance(ExportadorCSV(), ExportadorRelatorio)
    assert isinstance(ExportadorHTML(), ExportadorRelatorio)


def test_nao_pode_instanciar_exportador_abstrato():
    with pytest.raises(TypeError):
        ExportadorRelatorio()
