# Vote Monitor Application

This project is a web application for monitoring bills and legislators. It is divided into **backend** and **frontend** modules, and can be run either **locally** or **via Docker**.

---

## Table of Contents

1. [Technologies](#technologies)  
2. [Backend Setup](#backend-setup)  
3. [Frontend Setup](#frontend-setup)  
4. [Running with Docker](#running-with-docker)  
5. [Running Locally](#running-locally)  
6. [Running Backend Unit Tests](#running-backend-unit-tests) 
7. [Scripts](#scripts)  

---

## Technologies

- **Backend:** Python 3.12, FastAPI, Uvicorn  
- **Frontend:** React, Hooks (useEffect, useState)  
- **Docker:** Docker & Docker Compose  
- **Other:** CORS, Axios (frontend API calls), Pandas/csv (optional CSV handling)  

---

## Backend Setup

1. **Install Python 3.12** if not installed.  

2. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

3. **Install dependencies:**
   ```bash
   pip install -r backend/requirements.txt

4. **Run backend locally:**
   ```bash
   uvicorn backend.api.main:app --reload
Backend will run at http://127.0.0.1:8000


## Frontend Setup

1. **Install Node.js and npm** (Node >=18 recommended).

2. **Navigate to the frontend folder:**
   ```bash
   cd frontend

3. **Install dependencies:**
   ```bash
   npm install

4. **Run frontend locally:**
   ```bash
   npm start

Frontend will run at http://localhost:3000

## Running with Docker

1. Make sure **Docker** and **Docker Compose** are installed.

2. Use the script to build images and start containers:
   ```bash
   ./run_docker.sh


3. The backend will run at http://0.0.0.0:8000 and the frontend at http://0.0.0.0:3000

## Running Locally

1. Use the script to setup virtual environments, install dependencies, and run the app locally:
   ```bash
   ./run_local.sh


2. The backend and frontend will run in development mode with live reload.

## Running Backend Unit Tests

1. Make sure the backend virtual environment is activated:
   ```bash
   source venv/bin/activate  # Linux/macOS/WSDL
   
2. Run tests with **pytest**:
   ```bash
   cd backend
   pytest

3. Optional: run with verbose output:
   ```bash
   pytest -v


**Notes:**
- All tests are located in the backend/tests folder.


## Scripts
**run_docker.sh**

- Builds Docker images for backend and frontend.
- Starts all services using Docker Compose.
- Intended for production-ready execution.

**run_local.sh**

- Creates a Python virtual environment for the backend.
- Installs all dependencies for backend and frontend.
- Runs backend and frontend locally in development mode.
- Ideal for active development with live reload.