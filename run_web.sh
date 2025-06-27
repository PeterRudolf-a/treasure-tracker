#!/bin/bash

echo "🔧 Starting Treasure Tracker full stack..."

# Activate virtual environment
source venv/Scripts/activate  # Adjust path for Mac/Linux if needed

# Start Flask backend (in background)
echo "🌐 Starting Flask server at http://localhost:5000..."
cd server
python app.py &
FLASK_PID=$!
cd ..

# Start static web server for web-ui (in background)
echo "🧭 Starting web frontend at http://localhost:8080..."
cd web-ui
python -m http.server 8080 &
WEB_PID=$!
cd ..

# Wait briefly before launching browser
sleep 2

# Open browser (cross-platform)
URL="http://localhost:8080/login.html"
echo "🌐 Opening browser at $URL"
if command -v xdg-open &> /dev/null; then
    xdg-open "$URL"  # Linux
elif command -v open &> /dev/null; then
    open "$URL"      # macOS
elif command -v start &> /dev/null; then
    start "$URL"     # Windows Git Bash (calls Windows shell)
else
    echo "⚠️  Could not detect OS to auto-open browser. Please open $URL manually."
fi

# Handle cleanup on Ctrl+C
trap "echo '🛑 Shutting down...'; kill $FLASK_PID $WEB_PID; exit" INT

# Keep script running until Ctrl+C
wait

