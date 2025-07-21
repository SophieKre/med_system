from sqlalchemy import Column, String, Integer, Text, ARRAY

from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Boolean, Text
from app.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    is_available = Column(Boolean, default=True)
    email = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class TriageCase(Base):
    __tablename__ = "triage_cases"

    id = Column(String, primary_key=True, index=True)  # task_id или uuid
    patient_id = Column(String, nullable=False)
    raw_input = Column(Text, nullable=False)           # исходный текст симптомов
    symptoms = Column(Text)                            # выделенные симптомы
    diagnosis = Column(String)                         # предварительный диагноз
    urgency = Column(String)                           # срочность: неотложный, срочный, плановый
    specialization = Column(String)                    # профиль врача
    doctor = Column(String)                            # ФИО назначенного врача
    created_at = Column(DateTime, default=datetime.utcnow)

# class PatientRequestDB(Base):
#     __tablename__ = "patient_requests"
    
#     id = Column(Integer, primary_key=True, index=True)
#     patient_id = Column(String, index=True)
#     symptoms = Column(Text)
#     urgency = Column(Integer)
#     diagnoses = Column(ARRAY(String))
#     assigned_doctor_id = Column(String)
#     status = Column(String, default="processing")

# class DoctorDB(Base):
#     __tablename__ = "doctors"
    
#     id = Column(String, primary_key=True)
#     name = Column(String)
#     specialization = Column(String)
#     current_patients = Column(Integer, default=0)
#     max_patients = Column(Integer, default=10)
#     telegram_id = Column(String)