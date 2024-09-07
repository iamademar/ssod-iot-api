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

# 1. Save Room Occupancy (POST):
```
curl -X POST http://3.27.174.228/api/save_room_occupancy/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Api-Key YOUR_API_KEY_HERE" \
  -d '{
    "room_name": "WZ320",
    "sensor_name": "sensor1",
    "presence_detected": true,
    "temperature": 23.5
  }'
```

# 2. Check Room Occupancy (GET):
```
curl -X GET http://3.27.174.228/api/check_room_occupancy/WZ320/ \
  -H "Authorization: Api-Key YOUR_API_KEY_HERE"
```

# 3. Get Latest Occupancy Logs (GET):
```
curl -X GET http://3.27.174.228/api/get_latest_occupancy_logs/ \
  -H "Authorization: Api-Key YOUR_API_KEY_HERE"
```

# 4. Get Latest Room Temperature (GET):
```
curl -X GET http://3.27.174.228/api/get_latest_room_temperature/WZ320/ \
  -H "Authorization: Api-Key YOUR_API_KEY_HERE"
```