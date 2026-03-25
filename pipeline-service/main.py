from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from services.ingestion import fetch_all_customers, upsert_customers
from models.customer import Customer

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/ingest")
def ingest(db: Session = Depends(get_db)):
    data = fetch_all_customers()
    upsert_customers(db, data)
    return {"status": "success", "records_processed": len(data)}

@app.get("/api/customers")
def get_customers(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    offset = (page - 1) * limit
    customers = db.query(Customer).offset(offset).limit(limit).all()

    return {
        "data": [c.__dict__ for c in customers],
        "page": page,
        "limit": limit
    }

@app.get("/api/customers/{id}")
def get_customer(id: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter_by(customer_id=id).first()

    if not customer:
        return {"error": "Not found"}

    return customer.__dict__