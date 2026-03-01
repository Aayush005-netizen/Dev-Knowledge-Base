# 🎬 Movie Data Collection via API — ML Dataset Pipeline

This project demonstrates how to fetch real-world movie data from a REST API and convert it into a structured, ML-ready dataset using Python and Pandas. Instead of relying on static CSV files, this project simulates how real industry ML pipelines collect and prepare live data programmatically.

---

## 🚀 Project Overview

Most beginner ML projects start with pre-cleaned datasets. This project goes a step further by building the dataset from scratch using an API — the way it's done in production environments.

**Pipeline:**
```
API Request → JSON Response → Python Processing → Pandas DataFrame → ML-Ready Dataset
```

**Workflow steps:**
1. Send HTTP GET requests to a movie API endpoint
2. Receive and parse JSON responses
3. Extract relevant fields from nested JSON
4. Convert data into a structured Pandas DataFrame
5. Export the dataset for reuse (e.g., Kaggle, local ML pipeline)

---

## 🧠 Key Learnings

**APIs & Client-Server Communication**
Understood how APIs act as a bridge between applications, enabling clean, structured data access without web scraping. Learned how HTTP requests and responses work, and how to interact with REST endpoints.

**JSON Handling in Python**
APIs return data in JSON format. Learned to parse JSON into Python dictionaries and extract only the required fields from nested structures.

**Python for API Calls**
Used the `requests` library to send GET requests, handle status codes, and process API responses reliably.

**DataFrame Creation**
Transformed raw API output into structured Pandas DataFrames, making the data ready for analysis and ML pipelines.

**Real-World ML Data Pipelines**
Understood why real ML systems depend on live data sources and how APIs enable automation, real-time collection, and scalable data ingestion.

---

## 🛠️ Tech Stack

- Python 🐍
- `requests` — HTTP calls
- `pandas` — Data structuring & export
- REST API — Data source
- JSON — Data format

---

## 📂 Project Workflow
```
flowchart LR
A[API Request] --> B[JSON Response]
B --> C[Data Extraction]
C --> D[Pandas DataFrame]
D --> E[ML-Ready Dataset]
```

---

## 📈 Why This Project Matters

Most beginners work only with static datasets. This project bridges the gap between learning ML and working in industry by covering the complete data collection pipeline — from a live API all the way to a structured, exportable dataset ready for training models.

✅ Live data collection &nbsp; ✅ Automated dataset creation &nbsp; ✅ ML-ready output
