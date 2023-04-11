from sqlalchemy.orm import Session
from . import models
from fastapi import UploadFile
import pandas as pd

# Geolocation
def get_location(db: Session, ip_base10: int):

    results = db.query(models.IP_Geolocation).filter(models.IP_Geolocation.ip_from <= ip_base10).filter(models.IP_Geolocation.ip_to >= ip_base10).first()

    if results is None:
        return None
    
    country = results.country
    return country


def upload_file(db: Session, file: UploadFile):

    # Load CSV and insert content to DB
    ## Prepare data
    df = pd.read_csv(file.file, header = None)
    df = df.rename({0:'ip_from', 1:'ip_to', 2:'country'}, axis=1)

    ## Upload data
    ### Truncate existing data
    db.execute('''TRUNCATE TABLE ip_geolocation''')
    db.commit()
    
    engine = db.get_bind()
    df.to_sql('ip_geolocation', con=engine, if_exists='append', index=False, index_label='id')