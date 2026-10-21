
from ecommerce.categoria import Categoria
from ecommerce.despesa import Despesa


class Orcamento:

    def __init__(
        self,
        categoria: Categoria,
        limite: float,
        lancamentos=None
    ) -> None:
        self.categoria = categoria
        self.limite = float(limite)
        self.lancamentos = lancamentos if lancamentos is not None else []

    def total_gasto(self) -> float:
        return sum(
            l.valor
            for l in self.lancamentos
            if isinstance(l, Despesa)
            and l.categoria.nome == self.categoria.nome
        )

    def valor_restante(self) -> float:
        return self.limite - self.total_gasto()

    def estourou_limite(self) -> bool:
        return self.total_gasto() > self.limite
