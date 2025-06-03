from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    value = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
