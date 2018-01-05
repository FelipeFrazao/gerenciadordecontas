class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero: int = numero
        self.titular: str = titular
        self.saldo: float = saldo
        self.limite: float = limite