#!/bin/bash
set -e

echo "========================================="
echo " 🐳 Vote Monitor - Docker Setup"
echo "========================================="

ROOT_DIR=$(pwd)
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"

echo ""
echo "📁 Project directory: $ROOT_DIR"
echo ""

#############################################
# 1. Backend (venv just to freeze dependencies)
#############################################

echo "========================================="
echo " 🐍 Preparing Backend"
echo "========================================="

cd "$BACKEND_DIR"

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate

#############################################
# 2. Frontend
#############################################

echo ""
echo "========================================="
echo " ⚛️ Preparing Frontend"
echo "========================================="

cd "$FRONTEND_DIR"
npm install
npm run build

#############################################
# 3. Docker build
#############################################

echo ""
echo "========================================="
echo " 🐳 Building Docker Images"
echo "========================================="

cd "$ROOT_DIR"

docker build -f Dockerfile.backend -t vote-monitor-backend .
docker build -f Dockerfile.frontend -t vote-monitor-frontend .

#############################################
# 4. Docker compose up
#############################################

echo ""
echo "========================================="
echo " 🚀 Launching Containers"
echo "========================================="

docker compose up -d --build

echo ""
echo "========================================="
echo " ✅ Setup Complete!"
echo " Backend:  http://localhost:8000"
echo " Frontend: http://localhost:3000"
echo "========================================="
