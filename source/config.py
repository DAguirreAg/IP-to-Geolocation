import os

class Config:
    
    # DB settings
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/ip_to_geolocation_db'

    # App settings
    ## Metadata 
    DESCRIPTION = '''
    IP-To-Geolocation App is a simplified implementation of any Geolocation services based on IP found on the internet.
    '''

    TAGS_METADATA = [
        {
            "name": "Geolocation",
            "description": "Operations with IP and Geolocation. Includes the creation the retrieval of a the country from the input IP as well as a utility endpoint to facilitate the upload of the data in the database.",
        }    ]

    TITLE="Ip-to-Geolocation App"
    VERSION="0.0.1"
    CONTACT={
            "name": "DAguirreAg",
            "url": "https://github.com/DAguirreAg/"
            }
    LICENSE_INFO={
                "name": " MIT License",
                "url": "https://mit-license.org/",
                }