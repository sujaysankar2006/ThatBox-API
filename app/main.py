from fastapi import FastAPI

from app.database import Base,engine
from app import models
from router import cart,order,product,thatbox

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ThatBox API",
    description="Gift Schedluing and e-commerce application",
    version="1.0.0"
)
app.include_router(product.router)
app.include_router(cart.router)
app.include_router(order.router)
app.include_router(thatbox.router)

@app.get("/")
def health():
    return {"message :  good working condition..."}