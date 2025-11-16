# Vote Monitor

**Vote Monitor** is a system for tracking and analyzing congressional votes, built with Python and FastAPI on the backend, and ReactJS on the frontend.  
The system allows you to query:

1. For each legislator: how many bills they supported and how many they opposed.
2. For each bill: how many legislators supported it, how many opposed it, and who the primary sponsor is.

---

## 📂 Project Structure
```
vote-monitor
├── requirements.txt
├── README.md
├── backend
│ ├── api
│ │ ├── main.py
│ │ └── routes/
│ ├── data
│ │ ├── bills.csv
│ │ ├── legislators.csv
│ │ ├── votes.csv
│ │ └── vote_results.csv
│ ├── domain
│ ├── infrastructure
│ ├── interfaces
│ ├── services
│ ├── tests
│ └── utils
├── frontend
└── config
└── settings.yaml
```

---

## ⚡ Requirements

- Python 3.12+
- Virtualenv or conda
- Dependencies listed in `requirements.txt`

---

## 🛠️ Environment Setup

1. Create and activate the virtual environment:

```bash
python -m venv venv
source venv/bin/activate       # Linux / WSL
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Run the Tests

To run all tests:This will execute all unit tests inside backend/tests/.

```bash
pytest -vv
```

## 🚀 Run the Project (FastAPI)

Start the API:

```bash
uvicorn backend.api.main:app --reload
```

Available endpoints:

Returns, for each legislator, the total number of bills supported and opposed.

GET http://127.0.0.1:8000/legislators/summary

Returns, for each bill, the total number of supporters and opponents, and the primary sponsor.

GET http://127.0.0.1:8000/bills/summary
