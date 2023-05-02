# Environment setup
import requests
from datetime import datetime 
import io
import os
import pandas as pd
from sqlalchemy import create_engine

# Settings
## Input/Output
URL = "https://cdn.jsdelivr.net/npm/@ip-location-db/geolite2-country/geolite2-country-ipv4-num.csv"
FILENAME_PREFIX = "geolite2-country-ipv4-num"
OUTPUT_FOLDER = "files"
OUTPUT_SCHEMA = {
    'ip_from' : 'int64',
    'ip_to' : 'int64',
    'country_code' : 'object'
}

## Database
SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@localhost:5432/db_ip_to_geolocation'

## Misc.
SAVE_CSV = True

def get_csv_from_url(url):
    
    # Download file
    r = requests.get(url, allow_redirects=True)
    
    return r.content

def save_file_to_csv(content):
    
    # Generate filename
    ## Get current datetime
    dt = str(datetime.now())

    ## Reformat datetime string
    dt = dt.split(".")[0].replace(" ", "_").replace("-", "").replace(":", "")

    filename = FILENAME_PREFIX + "_" +  dt + ".csv"
    
    # Create CSV file
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    open(filepath, 'wb').write(content)

def convert_csv_to_datatframe(content):
    
    # Read file and convert to right format
    dff = pd.read_csv(io.StringIO(content.decode('utf-8')), header=None)
    dff = dff.rename({0:'ip_from', 1:'ip_to', 2:'country_code'}, axis=1)
    
    return dff

def validate_data(dff):
    
    # Check same amount of columns
    if len(OUTPUT_SCHEMA) != len(dff.columns):
        raise Exception("Mismatching amount of columns found.")
        
    # Check column names are correct
    for column in OUTPUT_SCHEMA.keys():
        if column not in dff.columns:
            raise Exception(f"Column missing: {column}")
    
    # Check column datatypes
    for column, dtype in OUTPUT_SCHEMA.items():
        if OUTPUT_SCHEMA[column] != dff[column].dtype:
            raise Exception(f"Mismatching datatype in column {column}. Expected {OUTPUT_SCHEMA[column]} but got {dff[column]}")    

def insert_data_into_db(dff):
    
    # Connect to DB and insert data
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    dff.to_sql('ip_geolocation', con=engine, if_exists='append', index=False, index_label='id')

if __name__ == "__main__":
    
    # Get CSV data
    content = get_csv_from_url(URL)
    
    # Save file as CSV
    if SAVE_CSV:
        save_file_to_csv(content)
    
    # Transform data
    df = convert_csv_to_datatframe(content)
    
    # Data quality checks
    validate_data(df)
    
    # Upload data to 
    insert_data_into_db(df)
