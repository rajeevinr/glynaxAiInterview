import requests
from sqlalchemy.orm import Session
from models.customer import Customer

def fetch_all_customers():
    page = 1
    all_data = []

    while True:
        res = requests.get(f"http://mock-server:5000/api/customers?page={page}&limit=10")
        data = res.json()

        if not data["data"]:
            break

        all_data.extend(data["data"])
        page += 1

    return all_data


def upsert_customers(db: Session, customers):
    for c in customers:
        existing = db.query(Customer).filter_by(customer_id=c["customer_id"]).first()

        if existing:
            for key, value in c.items():
                setattr(existing, key, value)
        else:
            new_customer = Customer(**c)
            db.add(new_customer)

    db.commit()