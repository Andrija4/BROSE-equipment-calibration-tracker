from sqlalchemy import Column, Integer, String, Date, Boolean
from datetime import date, timedelta
from .database import Base

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    brose_sap = Column(String, nullable=False, unique=True)
    serial_number = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=False)
    responsible_person = Column(String, nullable=True)
    last_calibration = Column(Date, nullable=False)
    interval_days = Column(Integer, nullable=False)
    calibration_location = Column(String, nullable=False)
    calibration_provider = Column(String, nullable=True)
    calibration_price = Column(Integer, nullable=True)
    email_sent_30_days = Column(Boolean, default=False)
    email_sent_7_days = Column(Boolean, default=False)
    email_sent_expired = Column(Boolean, default=False)
    is_calibrating = Column(Boolean, default=False)

    @property
    def next_calibration(self):
        return self.last_calibration + timedelta(days=self.interval_days)
    
    @property
    def status(self):
        if self.is_calibrating:
            return "CALIBRATING"
        days_left = (self.next_calibration - date.today()).days
        if days_left < 0:
            return "EXPIRED"
        elif days_left <= 30:
            return "DUE SOON"
        else:
            return "OK"
 
class Mail(Base):
    __tablename__ = "recipients"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)