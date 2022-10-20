from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from database import crud 

router = APIRouter(
    #prefix="/",
    tags=["Geolocation"],
    responses={404: {"description": "Not found"}}
)

@router.get('/get_geolocation')
def get_geolocation(ip: str, db: Session = Depends(get_db)):

    # Convert IP to number
    octets = [int(i) for i in ip.split('.')]
    ip_base10 = octets[0]*16777216 + octets[1]*65536 + octets[2]*256 + octets[3]*1

    # Find IP's geolocation
    country = crud.get_location(db, ip_base10)

    return {'country': country}