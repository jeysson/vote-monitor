#!/bin/bash
set -e

echo "========================================="
echo " 💻 Vote Monitor - Local Setup"
echo "========================================="

ROOT_DIR=$(pwd)
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"

echo ""
echo "📁 Project directory: $ROOT_DIR"
echo ""

#############################################
# 1. Backend
#############################################

echo "========================================="
echo " 🐍 Setting up Backend"
echo "========================================="

cd "$BACKEND_DIR"

echo "➡️ Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "➡️ Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "➡️ Starting backend in background..."
nohup uvicorn backend.api.main:app --reload --host 0.0.0.0 --port 8000 > backend.log 2>&1 &

deactivate

#############################################
# 2. Frontend
#############################################

echo ""
echo "========================================="
echo " ⚛️ Setting up Frontend"
echo "========================================="

cd "$FRONTEND_DIR"

echo "➡️ Installing dependencies..."
npm install

echo ""
echo "➡️ Starting frontend in background..."
nohup npm start > frontend.log 2>&1 &

#############################################
# 3. Final message
#############################################

echo ""
echo "========================================="
echo " ✅ Local environment is running!"
echo "-----------------------------------------"
echo " Backend:  http://localhost:8000"
echo " Frontend: http://localhost:3000"
echo " Logs:"
echo "    backend/backend.log"
echo "    frontend/frontend.log"
echo "========================================="
