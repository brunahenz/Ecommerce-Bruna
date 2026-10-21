class Conta:
    def __init__(self, nome: str, saldo_inicial: float = 0.0):
        self.__nome = nome
        self.__saldo = float(saldo_inicial)
        self.__lancamentos = []

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def lancamentos(self) -> list:
        return self.__lancamentos.copy()

    def adicionar_lancamento(self, lancamento) -> None:
        if lancamento in self.__lancamentos:
            raise ValueError("Esse lançamento já foi adicionado.")

        lancamento.aplicar(self)
        self.__lancamentos.append(lancamento)

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.__saldo += valor

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= valor
