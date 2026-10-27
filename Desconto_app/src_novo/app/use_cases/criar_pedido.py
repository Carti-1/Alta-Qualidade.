from ..entities.pedido import Pedido
from ..entities.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from ..gateways.pedido_gateway import IPedidoGateway
from ..dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from ..dtos.criar_pedido_output_dto import CriarPedidoOutputDTO


class CriarPedido:
    def __init__(self, pedido_gateway: IPedidoGateway):
        self.pedido_gateway = pedido_gateway

    def executar(self, input_dto: CriarPedidoInputDTO) -> CriarPedidoOutputDTO:
        tipo_desconto = input_dto.tipo_desconto.lower().strip()
        if tipo_desconto == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")

        pedido = Pedido(input_dto.cliente, input_dto.valor_original, desconto)
        self.pedido_gateway.salvar(pedido, tipo_desconto)

        valor_desconto = desconto.calcular(input_dto.valor_original)
        return CriarPedidoOutputDTO(
            cliente=input_dto.cliente,
            valor_original=input_dto.valor_original,
            valor_desconto=valor_desconto,
            valor_final=input_dto.valor_original - valor_desconto,
            tipo_desconto=tipo_desconto,
        )

    def listar_pedidos(self) -> list[CriarPedidoOutputDTO]:
        output_dtos = []
        for registro in self.pedido_gateway.listar():
            pedido = registro["pedido"]
            tipo_desconto = registro["tipo_desconto"]
            valor_desconto = pedido.desconto.calcular(pedido.valor_original)
            output_dtos.append(
                CriarPedidoOutputDTO(
                    cliente=pedido.cliente,
                    valor_original=pedido.valor_original,
                    valor_desconto=valor_desconto,
                    valor_final=pedido.valor_original - valor_desconto,
                    tipo_desconto=tipo_desconto,
                )
            )
        return output_dtos
