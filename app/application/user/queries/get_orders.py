from dataclasses import dataclass
from typing import Optional,List


@dataclass
class GetOrdersQuery:
    """获取订单列表查询参数"""
    user_id: int
    page: Optional[int] = 1
    page_size: Optional[int] = 10

@dataclass
class OrderDTO:
    """订单DTO"""
    id: int
    order_no: str
    total_amount: float
    status: str
    create_time: str
    update_time: str

@dataclass
class GetOrdersUseResult:
    """获取订单列表结果"""
    total: int
    orders: List[OrderDTO]


class GetOrdersHandler:
    """获取订单列表处理器"""
    #这里是为了简化使用了假数据
    # def __init__(self, order_repository: IOrderRepository):
    #     self.order_repository = order_repository

    async def handle(self, query: GetOrdersQuery) -> GetOrdersUseResult:
        """处理获取订单列表查询参数"""
        if query.user_id <= 0:
            raise ValueError('用户ID不能小于等于0')

        if query.page <= 0:
            raise ValueError('页码不能小于等于0')
        if query.page_size <= 0:
            raise ValueError('页大小不能小于等于0')
        orders=[
            OrderDTO(
                id=1,
                order_no='2022010100001',
                total_amount=100.00,
                status='待支付',
                create_time='2022-01-01 00:00:00',
                update_time='2022-01-01 00:00:00'
            ),
            OrderDTO(
                id=2,
                order_no='2022010100002',
                total_amount=200.00,
                status='待支付',
                create_time='2022-01-01 00:00:00',
                update_time='2022-01-01 00:00:00'
            ),
            OrderDTO(
                id=3,
                order_no='2022010100003',
                total_amount=300.00,
                status='待支付',
                create_time='2022-01-01 00:00:00',
                update_time='2022-01-01 00:00:00'
            )
        ]

        # 应用分页
        total=len(orders)
        # orders=orders[(query.page-1)*query.page_size:query.page*query.page_size]
        return GetOrdersUseResult(total=total, orders=orders)





