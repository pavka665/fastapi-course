from fastapi import APIRouter, Depends
from app.bookings.dao import Bookings
from app.bookings.schemas import SBooking
from app.users.models import Users
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix='/booking',
    tags=['Брони']
)

@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await Bookings.find_all(user_id=user.id)


