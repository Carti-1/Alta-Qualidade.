from ..entities.pedido import Pedido
from ..entities.desconto import DescontoNormal, DescontoVIP, DescontoPremium


class CriarPedido:
    def executar(self, cliente: str, valor_original: float, tipo_desconto: str) -> Pedido:
        tipo = tipo_desconto.lower()
        if tipo == "normal":
            desconto = DescontoNormal()
        elif tipo == "vip":
            desconto = DescontoVIP()
        elif tipo == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")

        return Pedido(cliente, valor_original, desconto)
