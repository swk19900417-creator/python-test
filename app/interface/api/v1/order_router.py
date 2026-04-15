from typing import List

from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import BaseModel

from app.application.common.exception import DomainException
from app.application.user.queries.get_orders import GetOrdersHandler, GetOrdersQuery
from app.interface.dependency import get_orders_handler

order_router=APIRouter(prefix="/orders",tags=["订单"])

class OrderResponse(BaseModel):
    id: int
    order_no: str
    total_amount: float
    status: str
    create_time: str
    update_time: str

class GetOrderResponse(BaseModel):
    total: int
    orders: List[OrderResponse]


@order_router.get("/",response_model=GetOrderResponse,status_code=status.HTTP_200_OK)
async def get_orders(user_id: int, page: int = 1, page_size: int = 10, handler: GetOrdersHandler = Depends(get_orders_handler)):
    """获取订单列表"""
    try:
        query = GetOrdersQuery(user_id=user_id, page=page, page_size=page_size)
        result = await handler.handle(query)
        return GetOrderResponse(total=result.total, orders=[OrderResponse(
            id=order.id,
            order_no=order.order_no,
            total_amount=order.total_amount,
            status=order.status,
            create_time=order.create_time,
            update_time=order.update_time
        ) for order in result.orders])
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))



