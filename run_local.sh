#!/bin/bash

echo "🚀 Starting Treasure Tracker locally..."

# Start Flask API in background
echo "🌐 Launching Flask server..."
cd server
source venv/Scripts/activate
python app.py &
SERVER_PID=$!
cd ..

# Start Pygame client
echo "🎮 Launching Pygame client..."
cd client
source venv/Scripts/activate
python main.py
cd ..

# After game is closed, stop Flask server
echo "🛑 Shutting down Flask server (PID: $SERVER_PID)"
kill $SERVER_PID

echo "✅ Everything stopped. Goodbye!"
