class Categoria:
    def __init__(self, nome: str):
        if not nome or not nome.strip():
            raise ValueError("O nome da categoria não pode ser vazio.")
        self.__nome = nome.strip()

    @property
    def nome(self) -> str:
        return self.__nome