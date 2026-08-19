import pytest
from ecommerce.conta import Conta


class TestConta:

    def test_criar_conta_com_sucesso(self):
        conta = Conta("Bruna", 100.0)
        assert conta.nome == "Bruna"
        assert conta.saldo == 100.0

    def test_criar_conta_saldo_padrao_zero(self):
        conta = Conta("Bruna")
        assert conta.saldo == 0.0

    def test_depositar_dinheiro(self):
        conta = Conta("Bruna", 50.0)
        conta.depositar(50.0)
        assert conta.saldo == 100.0

    def test_depositar_valor_invalido_lanca_excecao(self):
        conta = Conta("Bruna", 50.0)
        with pytest.raises(ValueError, match="O valor do depósito deve ser positivo."):
            conta.depositar(0)

    def test_sacar_dinheiro(self):
        conta = Conta("Bruna", 100.0)
        conta.sacar(40.0)
        assert conta.saldo == 60.0

    def test_sacar_valor_invalido_lanca_excecao(self):
        conta = Conta("Bruna", 100.0)
        with pytest.raises(ValueError, match="O valor do saque deve ser positivo."):
            conta.sacar(-10.0)

    def test_erro_saque_maior_que_saldo(self):
        conta = Conta("Bruna", 50.0)
        with pytest.raises(ValueError, match="Saldo insuficiente."):
            conta.sacar(100.0)