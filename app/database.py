from sqlalchemy.orm import Session
# from app.db_models import PatientRequestDB
# from app.database.session import get_db
# import os
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///test.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///test.db")

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def save_request(patient_id: str, symptoms: str, analysis: dict):
#     db: Session = next(get_db())
#     try:
#         db_request = PatientRequestDB(
#             patient_id=patient_id,
#             symptoms=symptoms,
#             urgency=analysis["urgency"],
#             diagnoses=analysis["diagnoses"],
#             assigned_doctor_id=None
#         )
#         db.add(db_request)
#         db.commit()
#         db.refresh(db_request)
#         return db_request
#     except Exception as e:
#         db.rollback()
#         raise e
#     finally:
#         db.close()