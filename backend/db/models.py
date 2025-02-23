from sqlalchemy import (
    Column, Integer, String, DateTime, DECIMAL, Boolean,
)
from .session import Base


class CarAd(Base):
    __tablename__ = "cars_ads"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String)
    title = Column(String)
    state = Column(Boolean)
    posted = Column(DateTime)
    expire = Column(DateTime)
    offer_type = Column(String)
    price = Column(DECIMAL)
    currency = Column(String)
    region = Column(String)
    phone_numbers = Column(String)
    color = Column(String)
    transport_year = Column(Integer)
    brand = Column(String)
    model = Column(String)
    transmission = Column(String)
    body = Column(String)
    engine_volume = Column(Integer)
    mileage = Column(Integer)
    drive = Column(String)
    country = Column(String)
    seller_type = Column(String)
    rudder = Column(String)
    availability = Column(String)
    origin = Column(String)
    generation = Column(String)
    