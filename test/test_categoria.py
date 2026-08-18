import pytest
from ecommerce.categoria import Categoria


class TestCategoria:

    def test_criar_categoria_gastos(self) -> None:
        categoria = Categoria("Alimentação")
        assert categoria.nome == "Alimentação"

    def test_criar_categoria_com_espacos(self):
        categoria = Categoria("  Transporte  ")
        assert categoria.nome == "Transporte"

    def test_nao_criar_categoria_nome_vazio(self):
        with pytest.raises(ValueError, match="O nome da categoria não pode ser vazio."):
            Categoria("")