import csv
from queue import Empty
from unittest import signals
from sqlalchemy.orm import Session
from fastapi import UploadFile
from fastapi.responses import JSONResponse
from models.device_signal import DeviceSignal
from utils.signals_tree import Tree

def post_signals(file: UploadFile, db: Session):
    try:
        db.query(DeviceSignal).delete()

        csv_reader = csv.reader(file.file.read().decode('utf-8').splitlines())
        next(csv_reader)

        for row in csv_reader:
            db.add(DeviceSignal(name=row[0], mmspath=row[1]))
        db.commit()

        return JSONResponse(status_code=201, content={
            "meta": None,
            "data": {
                "message": "File successfully uploaded to the database",
                "filename": file.filename
            },
            "errors": None,
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={
            "meta": "Internal Server Error",
            "data": None,
            "errors": f"Error: The file was not uploaded to the database due to: {str(e)}"
        })

def get_model(db: Session):
    try:
        signals_db = db.query(DeviceSignal).all()
        
        tree = Tree('Signals')

        for signal in signals_db:
            parts = signal.mmspath.split('/')
            value = parts[1].split('$')

            if (0 <= len(value) <= 3):
                path = [parts[0]] + [value[0]] + [value[1]] + [value[2]]
            elif (4 <= len(value) <= 6):
                path = [parts[0]] + [value[0]] + [value[1]] + [value[2]] + [value[3]]
            elif (7 <= len(value) <= 10):
                path = [parts[0]] + [value[1]] + [value[3]] + [value[5]] + [value[6]]
            tree.insert(path)
                
        # tree_json = json.dumps(tree.to_dict(), indent=4)

        return JSONResponse(status_code=201, content={
            "meta": None,
            "data": tree.to_dict(),
            "errors": None,
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={
            "meta": "Internal Server Error",
            "data": None,
            "errors": f"Error: The file was not uploaded to the database due to: {str(e)}"
        })
