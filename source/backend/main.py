from fastapi import FastAPI
import uvicorn

from ip_to_geolocation import ip_to_geolocation_routes

app = FastAPI()

#engine = create_engine(Config.SQLALCHEMY_DATABASE_URL)
#models.Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(ip_to_geolocation_routes.router)

if __name__ == "__main__":
    uvicorn.run(app, port=1234, host='0.0.0.0', reload=True)

