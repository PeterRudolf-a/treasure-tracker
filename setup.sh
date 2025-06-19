#!/bin/bash

echo "🔧 Setting up Python virtual environments..."

# Set up client environment
echo "📁 Setting up client/venv..."
cd client
python -m venv venv
source venv/Scripts/activate
pip install pygame requests
pip freeze > requirements.txt
deactivate
cd ..

# Set up server environment
echo "📁 Setting up server/venv..."
cd server
python -m venv venv
source venv/Scripts/activate
pip install flask flask-cors
pip freeze > requirements.txt
deactivate
cd ..

echo "✅ Setup complete!"
