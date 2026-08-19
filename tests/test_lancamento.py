from datetime import datetime
from ecommerce.categoria import Categoria
from ecommerce.lancamento import Lancamento


class TestLancamento:

    def test_criar_lancamento_com_sucesso(self):
        categoria = Categoria("Alimentação")
        agora = datetime.now()
        
        lancamento = Lancamento(" Almoço ", 45.50, "Despesa", categoria, agora)

        assert lancamento.descricao == "Almoço"
        assert lancamento.valor == 45.50
        assert lancamento.tipo == "despesa"
        assert lancamento.categoria == categoria
        assert lancamento.categoria.nome == "Alimentação"
        assert lancamento.data == agora

    def test_criar_lancamento_sem_data_usa_data_atual(self):
        categoria = Categoria("Salário")
        lancamento = Lancamento(" Pagamento ", 3000.0, "Receita", categoria)

        assert lancamento.descricao == "Pagamento"
        assert lancamento.valor == 3000.0
        assert lancamento.tipo == "receita"
        assert isinstance(lancamento.data, datetime)