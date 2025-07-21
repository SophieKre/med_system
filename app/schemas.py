from pydantic import BaseModel
from typing import List, Optional

class PatientRequest(BaseModel):
    patient_id: str
    symptoms: str

# class AnalysisResult(BaseModel):
#     urgency: int
#     diagnoses: list[str]
#     specialization: str
#     key_symptoms: list[str]
class TriageSubmitResult(BaseModel):
    task_id: str
    status: str = "analyzing"         # можно Enum
    message: Optional[str] = None
    doctor: Optional[str] = "TBD"


# === Ответ после обработки задачи ===
class TriageResult(BaseModel):
    urgency: str                     # срочность: "неотложный", "срочный", "плановый"
    specialization: str              # определённая специализация
    diagnosis: str                   # диагноз
    key_symptoms: List[str]          # ключевые симптомы
    doctor: str
class DoctorAssignment(BaseModel):
    patient_id: str
    doctor_id: str
    status: str


# class SymptomInput(BaseModel):
#     patient_id: str
#     symptoms: str

# class TriageResult(BaseModel):
#     urgency: str
#     specialization: str
#     notes: str
#     doctor: str
