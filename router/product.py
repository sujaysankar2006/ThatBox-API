from fastapi import APIRouter , Depends,HTTPException
from sqlalchemy import select
from app.database import get_db
from app.models import Product
from app.schemas import ProductCreate,ProductResponse,StockUpdate
from services.inventory import get_product_or_404_error,check_inventory
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/products",tags=["Products"])

@router.post("",response_model=ProductResponse,status_code=201)
def create_product(data:ProductCreate,db:Session = Depends(get_db)):
    
    product = Product(**data.model_dump())
    db.add(product)
    try:
        db.commit()
    except IntegrityError :
        db.rollback()
        raise HTTPException(
            status_code=401,
            detail="product name already exists"
        )
    db.commit()
    db.refresh(product)
    return product
@router.get("",response_model=list[ProductResponse])
def lisiting_product(db:Session=Depends(get_db)):
    return db.scalars(select(Product)).all()
@router.get("/{product_id}",response_model=ProductResponse)
def get_product(product_id:int,db:Session=Depends(get_db)):
    return get_product_or_404_error(db,product_id)
@router.patch("/{product_id}/stock",response_model=ProductResponse)
def update_stock(product_id:int,data:StockUpdate,db:Session=Depends(get_db)):
    product = get_product_or_404_error(db,product_id)
    product.stock = data.quantity
    db.commit()
    db.refresh(product)
    return product
@router.delete("/delete/{product_id}",response_model=ProductResponse)
def delete_product_by_id(product_id:int,db:Session=Depends(get_db)):
    product = db.get(Product,product_id)
    db.delete(product)
    db.commit()
    return f"{product.name} product details deleted succesfully"

