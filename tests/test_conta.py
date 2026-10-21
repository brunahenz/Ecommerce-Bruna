
import pytest
from ecommerce.conta import Conta


class TestConta:

    def test_criar_conta_com_sucesso(self):
        conta = Conta("Maria", 100.0)
        assert conta.nome == "Maria"
        assert conta.saldo == 100.0

    def test_criar_conta_saldo_padrao_zero(self):
        conta = Conta("Maria")
        assert conta.saldo == 0.0

    def test_depositar_dinheiro(self):
        conta = Conta("Maria", 50.0)
        conta.depositar(50.0)
        assert conta.saldo == 100.0

    def test_depositar_valor_invalido_lanca_excecao(self):
        conta = Conta("Maria", 50.0)
        with pytest.raises(
            ValueError,
            match="O valor do depósito deve ser positivo."
        ):
            conta.depositar(0)

    def test_sacar_dinheiro(self):
        conta = Conta("Maria", 100.0)
        conta.sacar(40.0)
        assert conta.saldo == 60.0

    def test_sacar_valor_invalido_lanca_excecao(self):
        conta = Conta("Maria", 100.0)
        with pytest.raises(
            ValueError,
            match="O valor do saque deve ser positivo."
        ):
            conta.sacar(-10.0)

    def test_erro_saque_maior_que_saldo(self):
        conta = Conta("Maria", 50.0)
        with pytest.raises(ValueError, match="Saldo insuficiente."):
            conta.sacar(100.0)

    def test_adicionar_receita_atualiza_saldo_e_registra_lancamento(self):
        from ecommerce.categoria import Categoria
        from ecommerce.receita import Receita

        conta = Conta("Maria")
        categoria = Categoria("Salário")
        receita = Receita("Pagamento", 1000.0, categoria)

        conta.adicionar_lancamento(receita)

        assert conta.saldo == 1000.0
        assert receita in conta.lancamentos

    def test_adicionar_despesa_atualiza_saldo_e_registra_lancamento(self):
        from ecommerce.categoria import Categoria
        from ecommerce.despesa import Despesa

        conta = Conta("Maria", 500.0)
        categoria = Categoria("Alimentação")
        despesa = Despesa("Mercado", 100.0, categoria)

        conta.adicionar_lancamento(despesa)

        assert conta.saldo == 400.0
        assert despesa in conta.lancamentos

    def test_nao_adicionar_mesmo_lancamento_duas_vezes(self):
        from ecommerce.categoria import Categoria
        from ecommerce.receita import Receita

        conta = Conta("Maria")
        categoria = Categoria("Salário")
        receita = Receita("Pagamento", 1000.0, categoria)

        conta.adicionar_lancamento(receita)

        with pytest.raises(
            ValueError,
            match="Esse lançamento já foi adicionado."
        ):
            conta.adicionar_lancamento(receita)

        assert conta.saldo == 1000.0
        assert len(conta.lancamentos) == 1

    def test_despesa_sem_saldo_nao_registra_lancamento(self):
        from ecommerce.categoria import Categoria
        from ecommerce.despesa import Despesa

        conta = Conta("Maria", 50.0)
        categoria = Categoria("Alimentação")
        despesa = Despesa("Mercado", 100.0, categoria)

        with pytest.raises(ValueError, match="Saldo insuficiente."):
            conta.adicionar_lancamento(despesa)

        assert conta.nome == "Maria"
        assert conta.saldo == 50.0
        assert despesa not in conta.lancamentos
