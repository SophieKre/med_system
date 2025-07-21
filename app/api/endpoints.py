from fastapi import APIRouter, BackgroundTasks
from app.schemas import PatientRequest
from app.tasks import process_patient_request

router = APIRouter()

@router.post("/requests")
async def submit_request(
    request: PatientRequest, 
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        process_patient_request.delay,
        request.patient_id,
        request.symptoms
    )
    return {"status": "processing", "message": "Request accepted"}