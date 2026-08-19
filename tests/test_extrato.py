from ecommerce.categoria import Categoria
from ecommerce.lancamento import Lancamento
from ecommerce.extrato import Extrato


class TestExtrato:

    def test_extrato_vazio(self):
        extrato = Extrato()
        assert extrato.quantidade_lancamentos() == 0
        assert extrato.gerar_linhas() == []

    def test_gerar_linhas_extrato(self):
        cat = Categoria("Geral")
        l1 = Lancamento("Salário", 2500.0, "Receita", cat)
        l2 = Lancamento("Mercado", 200.0, "Despesa", cat)

        extrato = Extrato([l1, l2])

        assert extrato.quantidade_lancamentos() == 2
        linhas = extrato.gerar_linhas()
        assert linhas[0] == "Salário: +R$ 2500.00"
        assert linhas[1] == "Mercado: -R$ 200.00"