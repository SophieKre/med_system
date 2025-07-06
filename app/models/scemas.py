from pydantic import BaseModel

class PatientRequest(BaseModel):
    patient_id: str
    symptoms: str

class AnalysisResult(BaseModel):
    urgency: int
    diagnoses: list[str]
    specialization: str
    key_symptoms: list[str]

class DoctorAssignment(BaseModel):
    patient_id: str
    doctor_id: str
    status: str