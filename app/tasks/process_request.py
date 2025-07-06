from app.tasks.celery_app import celery_app
from app.core.llm_processor import analyze_symptoms
from app.core.doctor_manager import assign_doctor
from app.core.notification import notify_doctor, notify_patient
from app.database.crud import save_request

@celery_app.task
def process_patient_request(patient_id: str, symptoms: str):
    # Анализ симптомов
    analysis = analyze_symptoms(symptoms)
    
    # Сохранение в БД
    save_request(patient_id, symptoms, analysis)
    
    # Назначение врача
    doctor_id = assign_doctor(
        analysis["specialization"], 
        analysis["urgency"]
    )
    
    # Отправка уведомлений
    notify_doctor(doctor_id, patient_id, analysis)
    notify_patient(patient_id, doctor_id)