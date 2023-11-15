from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session
from services import signals_controller
from models.db_connection import get_db

router = APIRouter()

@router.post("/signals/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    res = signals_controller.post_signals(file, db)
    return res

@router.get("/signals/model")
async def upload_file(db: Session = Depends(get_db)):
    file_data = signals_controller.get_model(db)
    return file_data