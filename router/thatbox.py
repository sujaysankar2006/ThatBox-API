from fastapi import HTTPException,APIRouter,Depends
from sqlalchemy import Select
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import ThatBox
from app.schemas import ThatBoxCreate,ThatBoxResponse
from services.inventory import check_inventory
from datetime import datetime,date

router = APIRouter(prefix = "/thatbox",tags=["ThatBox"])

@router.post("",response_model=ThatBoxResponse,status_code=201)
def gift_thatbox(data:ThatBoxCreate,db:Session=Depends(get_db)):
    if data.occasion_date < date.today():
        raise HTTPException(
            status_code=404,
            detail="Occasion date cannot be in past "
        )
    check_inventory(db,data.product_id)

    gift = ThatBox(**data.model_dump())

    db.add(gift)
    db.commit()
    db.refresh(gift)
    return gift

@router.get("",response_model=list[ThatBoxResponse])
def viewing_thatbox(db:Session=Depends(get_db)):
    return db.scalars(Select(ThatBox)).all()

@router.get("/{gift_id}",response_model=ThatBoxResponse)
def get_gifts(gift_id:int,db:Session=Depends(get_db)):
    item = db.get(ThatBox,gift_id)
    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Gift not found"
        )
    return item