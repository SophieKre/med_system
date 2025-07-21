
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse
from celery.result import AsyncResult
from app.schemas import PatientRequest, TriageSubmitResult, TriageResult
from app.tasks import analyze_symptoms
from app.celery_worker import celery_app
from fastapi import HTTPException

app = FastAPI()
@app.post("/triage", response_model=TriageSubmitResult)
async def triage_patient(input_data: PatientRequest, background_tasks: BackgroundTasks):
    task = analyze_symptoms.delay(input_data.patient_id, input_data.symptoms)
    return {
        "task_id": task.id,
        "status": "analyzing",
        "message": f"Задача принята. Task ID: {task.id}",
        "doctor": "TBD"
    }



@app.get("/result/{task_id}", response_model=TriageResult)
async def get_triage_result(task_id: str):
    result = AsyncResult(task_id, app=celery_app)

    if not result.ready():
        raise HTTPException(status_code=202, detail="Ещё обрабатывается")

    if result.failed():
        raise HTTPException(status_code=500, detail="Ошибка обработки")

    data = result.result
    return TriageResult(**data)
