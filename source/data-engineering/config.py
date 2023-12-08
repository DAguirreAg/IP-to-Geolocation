class Config:
    
    # DATABASE SETTINGS
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/db_ip_to_geolocation'
    
    # COUNTRY DATA
    URL_COUNTRY_DATA = 'https://cdn.jsdelivr.net/npm/@ip-location-db/geolite2-country/geolite2-country-ipv4-num.csv'
    RAW_FOLDER_COUNTRY_DATA = './downloads/country_level_files/'
    FILENAME_PREFIX_COUNTRY_DATA = 'geolite2-country-ipv4-num'

    SCHEMA_COUNTRY_DATA = {
        'ip_from' : 'int64',
        'ip_to' : 'int64',
        'country_code' : 'object'
    }
    
    # CITY DATA
    '''
    URL_CITY_DATA = 'https://github.com/sapics/ip-location-db/raw/master/geolite2-city/geolite2-city-ipv4-num.csv.gz'
    RAW_FOLDER_CITY_DATA = './downloads/city_level_files/'
    FILENAME_PREFIX_CITY_DATA = 'geolite2-city-ipv4-num'
    
    SCHEMA_CITY_DATA = {
        'ip_from' : 'int64',
        'ip_to' : 'int64',
        'country_code' : 'object'
    }'''