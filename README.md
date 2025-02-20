# **Web service data analysing [999.md](https://999.md/ru)**
## **Overview**
>This project is a FastAPI-based web service designed to collect, store, and analyze data from the [999.md](https://999.md/ru) website. The system includes a web scraper, a database for storing collected data, and an analytics module with a web interface for visualization.

---

## Project Structure
```
📂 Web999.md/
    ├── 📂 api/                    #FastAPI Backend  
    │   ├── main.py                 # Entry point  
    │   ├── dependencies.py         # Common dependencies  
    │   ├── 📂 modules/             # Modular structure  
    │       ├── 📂 auth/            # Authentication (JWT)  
    │       ├── 📂 cars/            # Car data handling  
    │       ├── 📂 analytics/       # Data analytics and visualization
    │          
    ├── 📂 db/ 
    │   ├── models.py                   
    │   ├── session.py 
    │
    ├── 📂 scraper/                 # Web Scraper  
    │   ├── fetcher.py              # Fetch data using GraphQL  
    │   ├── parser.py               # Parse and clean data  
    │   ├── saver.py                # Store data in the database  
    │   ├── scheduler.py            # Automate data collection  
    ├── 📂 frontend/                # Web UI for visualization  
    │   ├── index.html              # Dashboard  
    │   ├── charts.js               # Data visualization  
    │   ├── api.js                  # API interaction  
    ├── requirements.txt            # Dependencies  
```
---

## **Key Features**
### **1️⃣ Data Collection**
- Asynchronous scraper using GraphQL requests.
- Automatic pagination for fetching multiple pages.
- Saves car data such as **name, year, price, engine capacity, transmission, and listing date**.

### **2️⃣ Backend API (FastAPI)**
- [ ] **User authentication** using JWT.
- [ ] **Car data management** with CRUD operations.
- [ ] **Analytics endpoints** for calculating price trends, average car prices, and availability statistics.

### **3️⃣ Data Analysis & Visualization**
- [ ] Computes **average car prices**, **price distribution**, and **trends over time**.
- [ ] Generates **charts** and **graphs** for visual insights.

---

## **Technology Stack**
- [ ] **Backend:** FastAPI, SQLAlchemy, 
- [ ] **Database:** SQLite > 
    - [ ] Postgresql
- [ ] **Scraper:** aiohttp, bs4 >
    - [ ] GraphQL queries
- [ ] **Security:** JWT authentication (OAuth2)
- [ ] **Frontend:** HTML, JavaScript (Charts.js for visualization)
    - [ ] React, React Nativ

---

## **How to Run**

### **1️⃣ Install Dependencies of envirament**
```bash 
gh repo clone MeTANs/Web999.md
```
**Create envirament**
```bash
python3 -m venv venv
source .venv/bin/activate
```
**Install Dependencies**
```bash
pip install -r requirements.txt
```
### **2️⃣ Start the FastAPI Server**
```bash
uvicorn api.main:app --reload
```
---

## **Next Steps**

+ ✅Enhance analytics with predictive modeling.
+ ✅Implement filtering and search features.
+ ✅Deploy using Docker and cloud hosting.
