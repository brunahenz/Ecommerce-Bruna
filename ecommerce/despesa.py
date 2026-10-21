
from datetime import datetime
from ecommerce.lancamento import Lancamento
from ecommerce.categoria import Categoria


class Despesa(Lancamento):
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
            "despesa",
            categoria,
            data
        )

    def aplicar(self, conta) -> None:
        conta.sacar(self.valor)
