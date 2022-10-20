import os

class Config:
    
    # DB settings
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/ip_to_geolocation_db'
