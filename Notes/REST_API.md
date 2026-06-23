# 🌐 REST API

> **Source:** Caleb Curry — REST API Crash Course (Python + Flask + SQLAlchemy)  
> **Stack:** Python · Flask · SQLAlchemy · SQLite · Postman

---

## Table of Contents

- [What is an API?](#what-is-an-api)
- [What is REST?](#what-is-rest)
- [Why Backend Server?](#why-backend-server)
- [JSON — Language of APIs](#json--language-of-apis)
- [HTTP Methods & CRUD](#http-methods--crud)
- [Consuming an API with Python](#consuming-an-api-with-python)
- [Building an API with Flask](#building-an-api-with-flask)
  - [Setup](#setup)
  - [Model Definition](#model-definition)
  - [Endpoints](#endpoints)
  - [Running the App](#running-the-app)
- [Full Request-Response Flow](#full-request-response-flow)
- [HTTP Status Codes](#http-status-codes)
- [Quick Reference](#quick-reference)
- [Interview Q&A](#interview-qa)

---

## What is an API?

An **API** (Application Programming Interface) is a bridge that allows two pieces of software to communicate.

- **Client** → Frontend (browser, mobile app)
- **Server** → Backend (handles logic, talks to DB)

The backend doesn't expose *everything* — developers carefully choose which parts to expose as **API endpoints**.

---

## What is REST?

**REST** = **Re**presentational **S**tate **T**ransfer

A specific type of API that transfers data over the internet via **URLs** (the `/` slashes you see in endpoints).

```
calebcurry.com/drinks/5
                ↑       ↑
             resource   id
```

---

## Why Backend Server?

> Classic interview question — know all 4 reasons.

| Reason | Explanation |
|---|---|
| 🔐 **Security** | Frontend (JS) has no concept of security. Backend handles auth & authorization. |
| 🔄 **Versatility** | One backend can power web, mobile, and desktop apps simultaneously. |
| 🧩 **Modularity** | Swap the backend without breaking the frontend — API contract stays consistent. |
| 🌍 **Interoperability** | Public APIs let other devs build on top of your data (e.g. StackOverflow API). |

---

## JSON — Language of APIs

**JSON** (JavaScript Object Notation) is the standard data exchange format for modern APIs.

Built on two structures:
- **Key-value pairs** → like a Python `dict`
- **Ordered lists** → like a Python `list`

```json
{
  "id": 1,
  "name": "Mango Lassi",
  "description": "A refreshing Indian drink",
  "available": true
}
```

> XML used to be popular but is largely replaced by JSON in modern projects.

---

## HTTP Methods & CRUD

| HTTP Method | CRUD Action | Use Case |
|---|---|---|
| `GET` | Read | Fetch data from server |
| `POST` | Create | Send new data to server |
| `PUT` | Update (full) | Replace entire resource |
| `PATCH` | Update (partial) | Update only specific fields |
| `DELETE` | Delete | Remove a resource |

> ⚠️ **PUT vs PATCH:** PUT replaces the *whole* object. PATCH updates *just one field*. This distinction is commonly asked in interviews.

---

## Consuming an API with Python

```python
import requests

# GET request to StackOverflow API
url = "https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow"
response = requests.get(url)

# response.json() returns a Python dict — JSON maps directly to dicts
for item in response.json()['items']:
    print(item['title'])
    print(item['link'])
    print()
```

> **Tool to know:** [Postman](https://www.postman.com/) — lets you make any HTTP request with custom headers and body, without writing a frontend.

---

## Building an API with Flask

### Setup

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate          # Linux/Mac
# .venv\Scripts\activate           # Windows

# Install dependencies
pip3 install flask flask-sqlalchemy

# Save dependencies
pip3 freeze > requirements.txt

# Create entry point
touch application.py
```

---

### Model Definition

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks.db'
db = SQLAlchemy(app)

# Model = a DB table
class Drink(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

# Create tables
with app.app_context():
    db.create_all()
```

---

### Endpoints

#### GET — Fetch all items

```python
@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()
    output = [{'name': d.name, 'description': d.description} for d in drinks]
    return jsonify({"drinks": output})
```

#### GET — Fetch one item by ID

```python
@app.route('/drinks/<int:id>', methods=['GET'])
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return jsonify({'name': drink.name, 'description': drink.description})
```

#### POST — Create a new item

```python
@app.route('/drinks', methods=['POST'])
def add_drink():
    data = request.get_json()
    new_drink = Drink(name=data['name'], description=data['description'])
    db.session.add(new_drink)
    db.session.commit()
    return jsonify({'message': 'Drink added!'}), 201
```

#### PUT — Update entire item

```python
@app.route('/drinks/<int:id>', methods=['PUT'])
def update_drink(id):
    drink = Drink.query.get_or_404(id)
    data = request.get_json()
    drink.name = data['name']
    drink.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Drink updated!'})
```

#### PATCH — Update one field

```python
@app.route('/drinks/<int:id>', methods=['PATCH'])
def patch_drink(id):
    drink = Drink.query.get_or_404(id)
    data = request.get_json()
    if 'description' in data:
        drink.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Drink patched!'})
```

#### DELETE — Remove an item

```python
@app.route('/drinks/<int:id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get_or_404(id)
    db.session.delete(drink)
    db.session.commit()
    return jsonify({'message': 'Drink deleted!'})
```

---

### Running the App

```bash
export FLASK_APP=application
export FLASK_ENV=development    # enables hot reload
flask run
```

App runs at: `http://127.0.0.1:5000`

---

## Full Request-Response Flow

```
Client (Browser / Mobile / Postman)
        │
        │  HTTP Request
        │  GET /drinks/5
        ▼
  ┌─────────────┐
  │  Flask App  │  ← Routing, logic, auth
  └──────┬──────┘
         │  Query
         ▼
  ┌──────────────┐
  │   Database   │  ← SQLite / PostgreSQL
  │  (SQLAlchemy)│
  └──────┬───────┘
         │  Result
         ▼
  ┌─────────────┐
  │  Flask App  │  ← Serialize to JSON
  └──────┬──────┘
         │  HTTP Response
         │  { "name": "Mango Lassi", ... }
         ▼
Client (gets JSON back)
```

---

## HTTP Status Codes

| Code | Meaning |
|---|---|
| `200` | OK — Success |
| `201` | Created — New resource added |
| `204` | No Content — Success, nothing returned |
| `400` | Bad Request — Invalid input |
| `401` | Unauthorized — Not authenticated |
| `403` | Forbidden — Not allowed |
| `404` | Not Found |
| `500` | Internal Server Error |

---

## Quick Reference

| Term | Meaning |
|---|---|
| API | Application Programming Interface |
| REST | Representational State Transfer |
| Endpoint | A specific URL exposed by the API (e.g. `/drinks/5`) |
| JSON | Data format — key-value pairs, like a Python dict |
| Flask | Python micro web framework |
| SQLAlchemy | Python ORM — maps DB tables to Python classes |
| ORM | Object Relational Mapper |
| Postman | Tool to manually test API requests |
| `request.get_json()` | Parses incoming JSON body in Flask |
| `jsonify()` | Converts Python dict to JSON response in Flask |
| `db.session.commit()` | Saves DB changes permanently |
| `get_or_404()` | Fetches record or returns 404 if not found |

---

## Interview Q&A

**Q: What is a REST API?**  
A REST API is an interface that allows software systems to communicate over HTTP using standard methods (GET, POST, PUT, DELETE). Data is exchanged in JSON via URLs called endpoints.

---

**Q: What is the difference between PUT and PATCH?**  
PUT replaces the entire resource. PATCH updates only specific fields. Example: use PATCH to update just a user's email without touching their name or password.

---

**Q: Why use a backend server instead of directly accessing the database from the frontend?**  
Four reasons: **Security** (frontend has no auth mechanism), **Versatility** (one backend serves all platforms), **Modularity** (backend can be swapped without frontend changes), **Interoperability** (API can be made public for third-party devs).

---

**Q: What is an API endpoint?**  
A specific URL path the backend exposes for clients to interact with. Example: `GET /drinks/5` fetches the drink with ID 5.

---

**Q: What does `get_or_404()` do in Flask?**  
It queries the DB for a record by primary key. If found, returns it. If not found, automatically returns a 404 HTTP response — no manual check needed.

---

**Q: What is the difference between `POST` and `PUT`?**  
POST **creates** a new resource (you don't know the ID yet). PUT **updates** an existing resource at a known URL (you specify the ID).

---

**Q: What tool do you use to test APIs without a frontend?**  
Postman — allows sending any HTTP request (GET, POST, PUT, DELETE) with custom headers, body, and auth tokens.

---

*Last updated: June 2026*