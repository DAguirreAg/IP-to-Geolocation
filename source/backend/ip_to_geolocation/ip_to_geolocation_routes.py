from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
import starlette.status as status
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
def get_geolocation(ip: str, ipDate: str | None = None, db: Session = Depends(get_db)):

    # Validate inputs
    # IP4 address
    try:
        ipaddress.IPv4Address(ip)
    except ipaddress.AddressValueError:
        return {'ERROR' : 'IP4 address not correct!'}

    ## Date
    if ipDate:
        try:
            ipDate = datetime.strptime(ipDate, '%Y-%m-%d')
        except Exception as e:
            return {'ERROR' : 'Date format not correct!'}

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
    
    country = results.country

    return {'countryCode': country}


@router.post("/new_geolocation_data")
def upload(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Check if it is a CSV
        if file.filename.split('.')[-1] != 'csv':
            raise Exception("There was an error uploading the file. Expected a CSV file format.")

        # Replace DB data with newer data
        ## Load CSV and prepare data
        df = pd.read_csv(file.file, header = None)
        df = df.rename({0:'ip_from', 1:'ip_to', 2:'country'}, axis=1)

        ## Upload data
        ### Truncate existing data
        #db.execute('''TRUNCATE TABLE ip_geolocation''')
        #db.commit()
        
        engine = db.get_bind()
        df.to_sql('ip_geolocation', con=engine, if_exists='append', index=False, index_label='id')


    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}