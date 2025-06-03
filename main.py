from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Reading

# Crear tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency para obtener DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/data")
def receive_data(name: str, value: float, db: Session = Depends(get_db)):
    reading = Reading(name=name, value=value)
    db.add(reading)
    db.commit()
    db.refresh(reading)
    return {"message": "Datos recibidos correctamente", "data_id": reading.id}
