from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
import starlette.status as status
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


@router.post("/upload")
def upload(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Check if it is a CSV
        if file.filename.split('.')[-1] != 'csv':
            raise Exception("There was an error uploading the file. Expected a CSV file format.")

        # Replace DB data with newer data
        crud.upload_file(db, file)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}