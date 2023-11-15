from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# Import models
from .device_signal import DeviceSignal
# import os
# url_db = os.getenv('URL_DB')

# Create the connection to the db
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    DeviceSignal.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
