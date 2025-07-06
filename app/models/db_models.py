from sqlalchemy import Column, String, Integer, Text, ARRAY
from app.database.session import Base

class PatientRequestDB(Base):
    __tablename__ = "patient_requests"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, index=True)
    symptoms = Column(Text)
    urgency = Column(Integer)
    diagnoses = Column(ARRAY(String))
    assigned_doctor_id = Column(String)
    status = Column(String, default="processing")

class DoctorDB(Base):
    __tablename__ = "doctors"
    
    id = Column(String, primary_key=True)
    name = Column(String)
    specialization = Column(String)
    current_patients = Column(Integer, default=0)
    max_patients = Column(Integer, default=10)
    telegram_id = Column(String)