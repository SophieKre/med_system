from sqlalchemy.orm import Session
from app.models.db_models import PatientRequestDB
from app.database.session import get_db

def save_request(patient_id: str, symptoms: str, analysis: dict):
    db: Session = next(get_db())
    try:
        db_request = PatientRequestDB(
            patient_id=patient_id,
            symptoms=symptoms,
            urgency=analysis["urgency"],
            diagnoses=analysis["diagnoses"],
            assigned_doctor_id=None
        )
        db.add(db_request)
        db.commit()
        db.refresh(db_request)
        return db_request
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()