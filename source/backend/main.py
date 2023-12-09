from fastapi import FastAPI
import uvicorn
from config import Config
from starlette.middleware.cors import CORSMiddleware
from ip_to_geolocation import ip_to_geolocation_routes

app = FastAPI()

# Main App
app = FastAPI(
    title=Config.TITLE,
    description=Config.DESCRIPTION,
    version=Config.VERSION,
    contact=Config.CONTACT,
    license_info=Config.LICENSE_INFO,
    openapi_tags=Config.TAGS_METADATA
)

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:5500"
    #"*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(ip_to_geolocation_routes.router)

if __name__ == "__main__":
    uvicorn.run(app, port=1234, host='0.0.0.0', reload=True)
