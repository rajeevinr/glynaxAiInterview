# Backend Developer Technical Assessment

## 📌 Project Overview

This project implements a **data pipeline using Docker** with three services:

* **Flask API (Mock Server)** → Provides customer data from a JSON file
* **FastAPI (Pipeline Service)** → Fetches and ingests data into database
* **PostgreSQL** → Stores customer data

### 🔄 Data Flow

Flask API → FastAPI Pipeline → PostgreSQL → API Response

---

## ⚙️ Tech Stack

* Python 3.10+
* Flask
* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker & Docker Compose

---

## 📁 Project Structure

```
project-root/
│
├── docker-compose.yml
├── README.md
│
├── mock-server/
│   ├── app.py
│   ├── data/customers.json
│   ├── Dockerfile
│   └── requirements.txt
│
└── pipeline-service/
    ├── main.py
    ├── models/customer.py
    ├── services/ingestion.py
    ├── database.py
    ├── Dockerfile
    └── requirements.txt
```

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

Make sure you have installed:

* Docker Desktop (running)
* Python 3.10+
* Git

---

### 2️⃣ Run the Project

```bash
docker-compose up --build
```

---

### 3️⃣ Verify Services

| Service      | URL                        |
| ------------ | -------------------------- |
| Flask API    | http://localhost:5000      |
| FastAPI      | http://localhost:8000      |
| Swagger Docs | http://localhost:8000/docs |

---

## 🧪 API Testing

### ✅ Flask Endpoints

#### Get Customers

```
GET /api/customers?page=1&limit=5
```

#### Get Single Customer

```
GET /api/customers/{id}
```

#### Health Check

```
GET /api/health
```

---

### ✅ FastAPI Endpoints

#### Ingest Data

```
POST /api/ingest
```

#### Get Customers

```
GET /api/customers?page=1&limit=5
```

#### Get Single Customer

```
GET /api/customers/{id}
```

---

## 🔄 Example Commands

### Ingest Data (PowerShell)

```powershell
Invoke-WebRequest -Uri "http://localhost:8000/api/ingest" -Method POST
```

### Get Customers

```bash
curl.exe http://localhost:8000/api/customers?page=1&limit=5
```

---

## 🗄️ Database Details

* Database: `customer_db`
* Table: `customers`

### Fields:

* customer_id (Primary Key)
* first_name
* last_name
* email
* phone
* address
* date_of_birth
* account_balance
* created_at

---

## 🐳 Docker Services

* **postgres** → Database service
* **mock-server** → Flask API
* **pipeline-service** → FastAPI

---

## ✅ Features Implemented

* JSON-based mock data
* Pagination support
* REST APIs (Flask & FastAPI)
* Data ingestion pipeline
* Upsert logic (insert/update)
* PostgreSQL integration
* Dockerized multi-service setup

---

## 🧹 Useful Commands

### Stop services

```bash
docker-compose down
```

### Rebuild project

```bash
docker-compose down -v
docker-compose up --build
```

### Check logs

```bash
docker-compose logs
```

---

## 📌 Notes

* Flask reads data from JSON file (not hardcoded)
* FastAPI handles pagination and ingestion
* PostgreSQL stores structured customer data
* Swagger UI available for easy API testing

---

## 🎯 Conclusion

This project demonstrates a complete backend pipeline including:

* API development
* Data ingestion
* Database integration
* Containerization using Docker

---
