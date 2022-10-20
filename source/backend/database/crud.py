from sqlalchemy.orm import Session
from . import models

# Geolocation
def get_location(db: Session, ip_base10: int):

    results = db.query(models.IP_Geolocation).filter(models.IP_Geolocation.ip_from <= ip_base10).filter(models.IP_Geolocation.ip_to >= ip_base10).first()

    if results is None:
        return None
    
    country = results.country
    return country
