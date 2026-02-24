from fastapi import FastAPI
from .database import engine_equipment, engine_mail, Base
from .routes import equipment

Base.metadata.create_all(bind=engine_equipment)
Base.metadata.create_all(bind=engine_mail)

app = FastAPI(title="Calibration Tracker")

app.include_router(equipment.router)