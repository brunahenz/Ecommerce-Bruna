
from abc import ABC, abstractmethod
from datetime import datetime
from ecommerce.categoria import Categoria


class Lancamento(ABC):

    def __init__(
        self,
        descricao: str,
        valor: float,
        tipo: str,
        categoria: Categoria,
        data: datetime = None
    ) -> None:
        if not descricao or not descricao.strip():
            raise ValueError("A descrição não pode ser vazia.")

        valor = float(valor)
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")

        if not isinstance(categoria, Categoria):
            raise TypeError("A categoria deve ser um objeto Categoria.")

        self.descricao = descricao.strip()
        self.valor = valor
        self.tipo = tipo.strip().lower()
        self.categoria = categoria
        self.data = data if data is not None else datetime.now()

    @abstractmethod
    def aplicar(self, conta) -> None:
        pass
