from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DeviceSignal(Base):
    __tablename__ = "deviceSignals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mmspath = Column(String, index=True)

    def __repr__(self):
        return f"<DeviceSignal(id={self.id}, name={self.name}, mmspath={self.mmspath})>"
