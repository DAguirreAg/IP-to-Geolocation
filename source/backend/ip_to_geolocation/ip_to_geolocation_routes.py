from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
import starlette.status as status
from typing import Optional
from dependencies import get_db
from sql_app import models
import pandas as pd
from datetime import datetime
import ipaddress

router = APIRouter(
    #prefix="/",
    tags=["Geolocation"],
    responses={404: {"description": "Not found"}}
)

@router.get('/geolocation')
def get_geolocation(ip: str, ipDate: Optional[str] = None, db: Session = Depends(get_db)):

    #def get_geolocation(ip: str, ipDate: str | None = None, db: Session = Depends(get_db)):
   

    # Validate inputs
    # IP4 address
    try:
        ipaddress.IPv4Address(ip)
    except ipaddress.AddressValueError:
        raise HTTPException(status_code=400, detail="IP4 address not correct")

    ## Date
    if ipDate:
        try:
            ipDate = datetime.strptime(ipDate, '%Y-%m-%d')
        except Exception as e:
            raise HTTPException(status_code=400, detail="Date format not correct")

    # Convert IP to number
    octets = [int(i) for i in ip.split('.')]
    ip_base10 = octets[0]*16777216 + octets[1]*65536 + octets[2]*256 + octets[3]*1

    # Find IP's geolocation
    if ipDate:
        results = db.query(models.IP_Geolocation).filter(models.IP_Geolocation.ip_from <= ip_base10).filter(models.IP_Geolocation.ip_to >= ip_base10).filter(models.IP_Geolocation.updated_at <= ipDate).order_by(models.IP_Geolocation.updated_at.desc()).first()
    else:
        results = db.query(models.IP_Geolocation).filter(models.IP_Geolocation.ip_from <= ip_base10).filter(models.IP_Geolocation.ip_to >= ip_base10).order_by(models.IP_Geolocation.updated_at.desc()).first()

    if results is None:
        return {'countryCode': 'Unknown'}
    
    countryCode = results.country_code

    return {'countryCode': countryCode}