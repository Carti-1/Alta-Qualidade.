from ..entities.desconto import IDesconto


class Pedido:
    def __init__(self, cliente: str, valor_original: float, desconto: IDesconto):
        self.cliente = cliente
        self.desconto = desconto
        self.valor_original = valor_original

    def valor_final(self) -> float:
        return self.valor_original - self.desconto.calcular(self.valor_original)
