from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Sequence, MetaData, Date, PrimaryKeyConstraint
from .database import Base, engine

class IP_Geolocation(Base):
    __tablename__ = 'ip_geolocation'

    ip_from = Column(Integer)
    ip_to = Column(Integer)
    country_code = Column(String)
    updated_at = Column(DateTime)

    PrimaryKeyConstraint(ip_from, ip_to, name='id')