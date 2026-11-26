from fastapi import Depends,HTTPException,APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.models import CartItem ,Product
from app.schemas import CartCreate,CartResponse
from services.inventory import check_inventory

router = APIRouter(prefix="/cart",tags=["Cart"])

@router.post("",response_model=CartResponse,status_code=201)
def add_to_cart(data:CartCreate,db:Session=Depends(get_db)):
    exisiting =  db.scalar(select(CartItem).where (CartItem.id == data.product_id) )
    new_quantity = data.quantity
    if exisiting:
        new_quantity+=exisiting.quantity
    check_inventory(db,data.product_id,new_quantity)
    if exisiting:
        exisiting.quantity=new_quantity
        item = exisiting
    else:
        item = CartItem(**data.model_dump())
        db.add(item)
    db.commit()
    db.refresh(item)
    return item
@router.get("")
def view_cart(db:Session=Depends(get_db)):
    result = []
    total = 0 
    data = db.scalars(select(CartItem)).all()
    for item in data:
        product = db.get(Product,item.product_id)
        if product is None:
            continue
        subtotal = product.price * item.quantity
        total+=subtotal
        result.append({
                "cart_item_id": item.id,
                "product_name": product.name,
                "price": product.price,
                "quantity": item.quantity,
                "subtotal": subtotal
        })
        return {"result":result,"total":total}

@router.delete("/{product_id}")
def remove_cart(product_id:int,db:Session=Depends(get_db)):
    item = db.get(CartItem,product_id)
    if item is None:
        raise HTTPException(status_code=401,detail="product not found")
    db.delete(item)
    db.commit()
    return{"message:Item removed succcefully"}

    
