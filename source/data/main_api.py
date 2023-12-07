from fastapi import FastAPI
from starlette.responses import RedirectResponse
import downloader_country_data
import etl_country_data

app = FastAPI()

@app.get("/")
def main():
    response = RedirectResponse(url='/docs')
    return response

@app.get("/download_country_data")
def download_country_data():
    downloader_country_data.main()
    return None

@app.get("/etl_country_data")
def etl_country_data_():
    etl_country_data.main()
    return None