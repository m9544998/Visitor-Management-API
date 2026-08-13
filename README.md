# Visitor Management API

A simple REST API built with **Flask** and **SQLite** to manage office visitors.

## Features

* Add Visitor
* View All Visitors
* Get Visitor By ID
* Update Visitor
* Delete Visitor

## Technologies

* Python 3
* Flask
* SQLite3

## Project Structure

```text
visitor-management-api/
│
├── app.py
├── visitors.db
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install flask
```

Run:

```bash
python app.py
```

Server:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint         |
| ------ | ---------------- |
| POST   | `/visitors`      |
| GET    | `/visitors`      |
| GET    | `/visitors/<id>` |
| PUT    | `/visitors/<id>` |
| DELETE | `/visitors/<id>` |

## Sample JSON

```json
{
    "visitor_name": "Maheen",
    "purpose": "Interview",
    "person_to_meet": "HR Manager",
    "status": "Waiting"
}
```

## Database

```sql
CREATE TABLE visitors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    visitor_name TEXT,
    purpose TEXT,
    person_to_meet TEXT,
    status TEXT
);
```

## Requirements

```text
Flask==3.1.0
```
# Authur
Maheen Asad
