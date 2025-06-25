#!/bin/bash
echo "🧹 Cleaning the database..."
rm -f server/db.sqlite3
echo "✅ Removed server/db.sqlite3"
echo "📦 Reinitializing..."
python -c 'from server.models import init_db; init_db()'
echo "✅ Database reinitialized in server/db.sqlite3."
