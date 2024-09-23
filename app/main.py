from fastapi import FastAPI 
from pydantic import BaseModel
from datetime import date
from app.bookings.router import router as router_booking
from app.users.router import router as router_user


class SUser(BaseModel):
    name: str
    age: int

class SHotel(BaseModel):
    hotel_id: int
    date_from: date
    date_to: date


app = FastAPI()
app.include_router(router_booking)
app.include_router(router_user)

