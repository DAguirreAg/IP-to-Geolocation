from sqlalchemy import Column, Integer, String, DateTime, Index, Boolean, ForeignKey, Sequence, MetaData, Date, PrimaryKeyConstraint
from .database import Base, engine

class IP_Geolocation(Base):
    __tablename__ = 'ip_geolocation'

    id = Column(Integer, primary_key=True, unique=True)
    ip_from = Column(Integer)
    ip_to = Column(Integer)
    country_code = Column(String)
    updated_at = Column(DateTime)

    __table_args__ = (Index('idx_ip_geolocation_ip_from_ip_to', "ip_from", "ip_to"), )