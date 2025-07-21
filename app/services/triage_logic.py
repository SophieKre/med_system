import openai
import json
from app.db_models import Doctor
from app.database import SessionLocal
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_prompt(symptoms: str) -> str:
    return f"""
    Жалобы пациента: {symptoms}

    1. Выдели ключевые симптомы.
    2. Сформулируй предварительный диагноз.
    3. Оцени срочность случая: неотложный, срочный, плановый.
    4. Укажи подходящую медицинскую специализацию.

    Ответ в формате JSON:
    {{
      "symptoms": ["..."],
      "diagnosis": "...",
      "urgency": "...",
      "specialization": "..."
    }}
    """

def call_llm(prompt: str) -> dict:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=500
    )
    reply = response.choices[0].message.content
    return json.loads(reply)

def find_doctor_by_specialization(specialization: str) -> str:
    db = SessionLocal()
    doctor = db.query(Doctor).filter_by(specialization=specialization, is_available=True).first()
    db.close()
    return doctor.full_name if doctor else "Нет доступных врачей"
