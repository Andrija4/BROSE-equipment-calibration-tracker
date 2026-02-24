from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_EQUIPMENT_URL = "sqlite:///./calibration.db"
DATABASE_MAIL_URL = "sqlite:///./mailing.db"

engine_equipment = create_engine(
    DATABASE_EQUIPMENT_URL, connect_args={"check_same_thread": False}
)
engine_mail = create_engine(
    DATABASE_MAIL_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine_equipment)
SessionLocalMail = sessionmaker(bind=engine_mail)
Base = declarative_base()