import httpx
from tenacity import retry, stop_after_attempt, wait_exponential
from app.config import settings
from app.utils.logging import logger

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1))
def analyze_symptoms(symptoms: str) -> dict:
    prompt = f"""
    [Medical Assistant Instructions]
    Analyze symptoms and return JSON with:
    - urgency (1-5 scale)
    - diagnoses (top 3 possible)
    - specialization (recommended doctor type)
    - key_symptoms (extracted clinical features)
    
    Patient symptoms: {symptoms}
    """
    
    try:
        with httpx.Client(timeout=30) as client:
            response = client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
                json={
                    "model": "gpt-4-turbo",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.1,
                    "response_format": {"type": "json_object"}
                }
            )
            return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        logger.error(f"LLM request failed: {str(e)}")
        return default_analysis()

def default_analysis():
    return {
        "urgency": 3,
        "diagnoses": ["Undefined"],
        "specialization": "general",
        "key_symptoms": []
    }