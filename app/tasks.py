from app.celery_worker import celery_app

from datetime import datetime

from app.celery_worker import celery_app
from app.database import SessionLocal
from app.db_models import TriageCase
from app.services.triage_logic import generate_prompt, call_llm, find_doctor_by_specialization


@celery_app.task
def analyze_symptoms(patient_id, symptoms):
    try:
        prompt = generate_prompt(symptoms)
        result = call_llm(prompt)
        doctor_name = find_doctor_by_specialization(result["specialization"])

        triage = TriageCase(
            id=f"{patient_id}_{datetime.utcnow().timestamp()}",
            patient_id=patient_id,
            raw_input=symptoms,
            symptoms=", ".join(result["symptoms"]),
            diagnosis=result["diagnosis"],
            urgency=result["urgency"],
            specialization=result["specialization"],
            doctor=doctor_name
        )

        db = SessionLocal()
        db.add(triage)
        db.commit()
        db.close()

        return  {
    "urgency": result["urgency"],
    "specialization": result["specialization"],
    "diagnosis": result["diagnosis"],                # исправлено
    "key_symptoms": result["symptoms"],              # это список
    "doctor": doctor_name
}


    except Exception as e:
        return {
    "urgency": 'error',
    "specialization":'error',
    "diagnosis": 'error',                # исправлено
    "key_symptoms": 'error',              # это список
    "doctor": 'error'
}

