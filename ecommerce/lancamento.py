from datetime import datetime
from ecommerce.categoria import Categoria


class Lancamento:

    def __init__(self, descricao: str, valor: float, tipo: str, categoria: Categoria, data: datetime = None) -> None:
        self.descricao = descricao.strip()
        self.valor = float(valor)
        self.tipo = tipo.strip().lower()
        self.categoria = categoria
        self.data = data if data is not None else datetime.now()