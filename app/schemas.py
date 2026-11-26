from pydantic import BaseModel, Field, ConfigDict
from typing import Literal
from decimal import Decimal
from datetime import datetime,date,time


class ProductCreate(BaseModel):
    name:str = Field(min_length=1,max_length=100)
    category:str
    description:str
    price:Decimal=Field(gt=0)
    available:bool
    stock:int = Field(gt=0)

class ProductResponse(ProductCreate):
    id:int
    model_config = ConfigDict(from_attributes=True)

class CartCreate(BaseModel):
    product_id:int
    quantity:int = Field(gt=0)
class CartResponse(BaseModel):
    id:int
    model_config = ConfigDict(from_attributes=True)
class StockUpdate(BaseModel):
    quantity:int
class BuyNowRequest(BaseModel):
    product_id:int
    quantity:int=Field(gt=0)
class OrderResponse(BaseModel):
    id:int
    product_id:int
    quantity:int = Field(gt=0)
    total_amount:Decimal
    status:str
    created_at:datetime

    model_config = ConfigDict(from_attributes=True)

AllowedState = Literal["Tamil Nadu","Andhra Pradhesh","Mumbai","Goa","Pondycherry","Teleganana","Madhya Pradhesh"]

class ThatBoxCreate(BaseModel):
    product_id:int
    occasion: str = Field(min_length=1)
    occasion_date: date
    gift_person_name:str = Field(min_length=3 , max_length=100)
    delivery_time:time
    state:AllowedState
    location:str
    gift_wrap:bool = False
    gift_note:str = " "

class ThatBoxResponse(ThatBoxCreate):
    id:int
    status:str

    model_config = ConfigDict(from_attributes=True)

