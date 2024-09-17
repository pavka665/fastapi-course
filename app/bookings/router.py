from fastapi import APIRouter
from app.bookings.dao import Bookings
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix='/booking',
    tags=['Брони']
)

@router.get('')
async def get_bookings() -> list[SBooking]:
    return await Bookings.find_all()


