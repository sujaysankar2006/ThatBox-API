from datetime import timezone,date,datetime
from sqlalchemy import (Integer,String,Boolean,ForeignKey,Text,DateTime,Date,Numeric,Time)
from sqlalchemy.orm import Mapped,mapped_column
from app.database import Base
from decimal import Decimal
from datetime import time

class Product(Base):
    __tablename__ = "products"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(100),unique=True)
    description:Mapped[str]=mapped_column(Text)
    category:Mapped[str]=mapped_column(String(100))
    price:Mapped[Decimal]=mapped_column(Numeric(10,2))
    available:Mapped[bool] = mapped_column(Boolean,default=True)
    stock:Mapped[int] = mapped_column(Integer,default=0)

class Order(Base):
    __tablename__ = "orders"
    id:Mapped[int] = mapped_column(primary_key=True)
    product_id:Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity:Mapped[int] = mapped_column(Integer)
    total_amount:Mapped[Decimal] = mapped_column(Numeric(10,2))
    status:Mapped[str] = mapped_column(String(30),default="confirmed")
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True),default=lambda:datetime.now(timezone.utc))

class CartItem(Base):
    __tablename__ = "cart_items"
    id:Mapped[int] = mapped_column(primary_key=True)
    product_id:Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity:Mapped[int] = mapped_column(Integer,default=1)

class ThatBox(Base):
    __tablename__ = "thatbox"
    id:Mapped[int] = mapped_column(primary_key=True)
    product_id:Mapped[int] = mapped_column(ForeignKey("products.id"))
    occasion: Mapped[str] = mapped_column(String(100))
    occasion_date: Mapped[date] = mapped_column(Date)
    location:Mapped[str]=mapped_column(Text)
    gift_person_name:Mapped[str] = mapped_column(String(100))
    delivery_time:Mapped[time]=mapped_column(Time)
    state:Mapped[str] = mapped_column(String(100))
    gift_wrap:Mapped[bool]=mapped_column(Boolean,default=False)
    gift_note:Mapped[str]=mapped_column(Text,default =" ")
    status:Mapped[str]=mapped_column(String(30),default="scheduled")
