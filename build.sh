#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python 3.11 if needed
if ! command -v python3.11 &> /dev/null; then
    echo "Python 3.11 not found, installing..."
    # This is handled by Render's build system
fi

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

python manage.py ensure_superuser

# Seed the database with sample data
python manage.py seed_data

echo "✅ Build completed successfully!"