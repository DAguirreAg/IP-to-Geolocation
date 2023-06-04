# Environment setup
import io
import pandas as pd
from sqlalchemy import create_engine
from utils import get_csv_from_url

# Settings
## Input/Output
URL = "https://cdn.jsdelivr.net/npm/@ip-location-db/geolite2-country/geolite2-country-ipv4-num.csv"
FILENAME_PREFIX = "geolite2-country-ipv4-num"
OUTPUT_FOLDER = "country_level_files"
OUTPUT_SCHEMA = {
    'ip_from' : 'int64',
    'ip_to' : 'int64',
    'country_code' : 'object'
}

## Database
SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/db_ip_to_geolocation'

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
            raise Exception(f"Mismatching datatype in column {column}. Expected {OUTPUT_SCHEMA[column]} but got {dff[column].dtype}")    

def insert_data_into_db(dff):
    
    # Connect to DB and insert data
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    dff.to_sql('ip_geolocation', con=engine, if_exists='append', index=False, index_label='id')

if __name__ == "__main__":
    
    # Get CSV data
    content = get_csv_from_url(URL)
    
    # Transform data
    df = convert_csv_to_datatframe(content)
    
    # Data quality checks
    validate_data(df)
    
    # Upload data to 
    insert_data_into_db(df)