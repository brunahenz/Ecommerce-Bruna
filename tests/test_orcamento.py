from ecommerce.categoria import Categoria
from ecommerce.lancamento import Lancamento
from ecommerce.orcamento import Orcamento


class TestOrcamento:

    def test_orcamento_dentro_do_limite(self):
        cat_alimentacao = Categoria("Alimentação")
        
        l1 = Lancamento("Mercado", 200.0, "Despesa", cat_alimentacao)
        l2 = Lancamento("Restaurante", 150.0, "Despesa", cat_alimentacao)

        orcamento = Orcamento(cat_alimentacao, 500.0, [l1, l2])

        assert orcamento.total_gasto() == 350.0
        assert orcamento.valor_restante() == 150.0
        assert orcamento.estourou_limite() is False

    def test_orcamento_estourado(self):
        cat_alimentacao = Categoria("Alimentação")
        
        l1 = Lancamento("Mercado", 400.0, "Despesa", cat_alimentacao)
        l2 = Lancamento("Jantar", 200.0, "Despesa", cat_alimentacao)

        orcamento = Orcamento(cat_alimentacao, 500.0, [l1, l2])

        assert orcamento.total_gasto() == 600.0
        assert orcamento.valor_restante() == -100.0
        assert orcamento.estourou_limite() is True