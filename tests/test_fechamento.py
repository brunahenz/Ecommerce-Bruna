
from ecommerce.categoria import Categoria
from ecommerce.receita import Receita
from ecommerce.despesa import Despesa
from ecommerce.fechamento import Fechamento


class TestFechamento:

    def test_fechamento_vazio(self):
        fechamento = Fechamento()
        assert fechamento.total_receitas() == 0.0
        assert fechamento.total_despesas() == 0.0
        assert fechamento.saldo_final() == 0.0

    def test_calcular_totais_e_saldo_final(self):
        cat_alimentacao = Categoria("Alimentação")
        cat_salario = Categoria("Salário")

        l1 = Receita("Salário", 3000.0, cat_salario)
        l2 = Despesa("Mercado", 250.0, cat_alimentacao)
        l3 = Receita("Freelance", 500.0, cat_salario)
        l4 = Despesa("Restaurante", 100.0, cat_alimentacao)

        fechamento = Fechamento([l1, l2, l3, l4])

        assert fechamento.total_receitas() == 3500.0
        assert fechamento.total_despesas() == 350.0
        assert fechamento.saldo_final() == 3150.0
