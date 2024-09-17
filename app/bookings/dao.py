from app.dao.base import BaseDAO
from app.bookings.models import Bookings


class Bookings(BaseDAO):
    model = Bookings