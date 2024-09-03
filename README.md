# Django REST Framework API

This project is a Django-based API using Django REST Framework.

## Setup and Installation

1. Ensure you have Python installed on your system.

2. Install the required packages:
   ```
   pip install django djangorestframework
   ```

3. Clone this repository:
   ```
   git clone [repository URL]
   cd [project directory]
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## API Documentation

The API is now accessible at `http://127.0.0.1:8000/`.

# Sending updates for presence
```
curl -X POST http://127.0.0.1:8000/api/sensor \
-H "Content-Type: application/json" \
-H "X-API-KEY: secret-key" \
-d '{
    "presence_detected": true,
    "room_name": "Room1",
    "temperature": 23.45
}'
```
