
from datetime import datetime
from ecommerce.lancamento import Lancamento
from ecommerce.categoria import Categoria


class Receita(Lancamento):
    def __init__(
        self,
        descricao: str,
        valor: float,
        categoria: Categoria,
        data: datetime = None
    ) -> None:
        super().__init__(
            descricao,
            valor,
            "receita",
            categoria,
            data
        )

    def aplicar(self, conta) -> None:
        conta.depositar(self.valor)
