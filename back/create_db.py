from models.device_signal import Base, engine

Base.metadata.create_all(bind=engine)