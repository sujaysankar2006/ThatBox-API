from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Product

def get_product_or_404_error(db:Session,product_id:int):
    product = db.get(Product,product_id)
    if product is None:
        raise HTTPException(
            status_code=404,
            detail= " product not fount retry"
        )
    return product
def check_inventory(db:Session,product_id:int,quantity:int=1):
    product= get_product_or_404_error(db,product_id)
    if not product.available or product.stock<quantity:
        raise HTTPException(
            status_code=409,
            detail="Insufficent Stock or Product Not Available"
        )
    return product