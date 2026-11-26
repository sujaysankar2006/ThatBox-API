
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Order
from app.schemas import BuyNowRequest,OrderResponse
from services.inventory import check_inventory

router = APIRouter(prefix="/orders",tags=["Orders"])

@router.post("",response_model=OrderResponse,status_code=201)
def buy_now(data:BuyNowRequest,db:Session=Depends(get_db)):
    product =check_inventory(db,data.product_id,data.quantity)
    total_amount = product.price*data.quantity
    product.stock -= data.quantity
    order = Order(
             product_id=product.id,
        quantity=data.quantity,
        total_amount=total_amount,
        status="confirmed"
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
@router.get("")
def listing_orders(db:Session=Depends(get_db)):
    order = db.scalars(select(Order)).all()
    return order
@router.get("{order_id}/invoice")
def invoice_generator(order_id:int,db:Session=Depends(get_db)):
    order = db.get(Order,order_id)
    if order is None:
        raise HTTPException(status_code=404,detail="order not found ")
    
    return {
        "invoice_number": f"INV-{order.id:06d}",
        "order_id": order.id,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "total_amount": order.total_amount,
        "status": order.status,
        "issued_at": order.created_at
    }
