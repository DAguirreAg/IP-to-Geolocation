# Environment setup
import pandas as pd
from sqlalchemy import create_engine
from config import Config
from utils import get_latest_file

def transform(dff):
    
    # Transform to right format
    dff = dff.rename({0:'ip_from', 1:'ip_to', 2:'country_code'}, axis=1)
    
    return dff

def validate_data(dff, output_schema):
    
    # Check same amount of columns
    if len(output_schema) != len(dff.columns):
        raise Exception("Mismatching amount of columns found.")
        
    # Check column names are correct
    for column in output_schema.keys():
        if column not in dff.columns:
            raise Exception(f"Column missing: {column}")
    
    # Check column datatypes
    for column, dtype in output_schema.items():
        if output_schema[column] != dff[column].dtype:
            raise Exception(f"Mismatching datatype in column {column}. Expected {output_schema[column]} but got {dff[column].dtype}")    

def insert_data_into_db(dff, sql_db_url):
    
    # Connect to DB and insert data
    engine = create_engine(sql_db_url)
    dff.to_sql('ip_geolocation_country', con=engine, if_exists='append', index=False, index_label='id')

def main():
    # Get CSV filename
    filename = get_latest_file(Config.RAW_FOLDER_COUNTRY_DATA)
    
    # Extract (Load file)
    df = pd.read_csv(filename, header=None)
    
    # Transform data
    df = transform(df)
        
    # Data quality checks
    validate_data(df, Config.SCHEMA_COUNTRY_DATA)
    
    # Load (Upload data)
    insert_data_into_db(df, Config.SQLALCHEMY_DATABASE_URL)

if __name__ == "__main__":
    main()
