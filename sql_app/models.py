from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .database import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)


class Room(Base):
    __tablename__ = 'rooms'

    room_id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String, unique=True, nullable=False, index=True)
    capacity = Column(Integer, nullable=False)


class Booking(Base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='SET NULL'), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.room_id', ondelete='SET NULL'), nullable=False)
    booked_num = Column(Integer, nullable=False)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)
