from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from freezegun import freeze_time
from .models import RoomOccupancy
from .services import is_room_occupied

class RoomOccupancyTests(TestCase):

    def setUp(self):
        self.room1 = "Room1"
        self.room2 = "Room2"
        self.sensor1 = "Sensor1"
        self.sensor2 = "Sensor2"
        self.now = timezone.now()
        self.frozen_time = timezone.now()

        # Create records for Room1
        RoomOccupancy.objects.create(room_name=self.room1, sensor_name=self.sensor1, presence_detected=False, temperature=22.5, timestamp=self.now - timedelta(minutes=2))
        RoomOccupancy.objects.create(room_name=self.room1, sensor_name=self.sensor2, presence_detected=False, temperature=22.5, timestamp=self.now - timedelta(minutes=4))
        
        # Create records for Room2
        RoomOccupancy.objects.create(room_name=self.room2, sensor_name=self.sensor1, presence_detected=True, temperature=22.5, timestamp=self.now - timedelta(minutes=2))
        RoomOccupancy.objects.create(room_name=self.room2, sensor_name=self.sensor2, presence_detected=True, temperature=22.5, timestamp=self.now - timedelta(minutes=1))

    def test_is_room_occupied_checks_specific_room(self):
        """
        Scenario 1: Verify that the function only checks the record for the specified room.
        Room2 has presence_detected as True within the last 3 minutes, so it should return True.
        Room1 has presence_detected as False within the last 3 minutes, so it should return False.
        """
        self.assertTrue(is_room_occupied(self.room2))
        self.assertFalse(is_room_occupied(self.room1))

    def test_is_room_occupied_checks_last_3_minutes(self):
        """
        Scenario 2: Verify that the function only checks the last 3 minutes.
        Adding a record for Room1 that is older than 3 minutes should not affect the result.
        """
        RoomOccupancy.objects.create(room_name=self.room1, sensor_name=self.sensor1, presence_detected=True, temperature=22.5, timestamp=self.now - timedelta(minutes=5))
        self.assertFalse(is_room_occupied(self.room1))

    def test_is_room_occupied_detects_presence_false(self):
        """
        Scenario 3: Verify that if it detects a presence_detected as False, then the room should return False on occupied.
        Adding a recent record for Room1 with presence_detected as False should result in False.
        """
        RoomOccupancy.objects.create(room_name=self.room1, sensor_name=self.sensor1, presence_detected=False, temperature=22.5, timestamp=self.now - timedelta(minutes=1))
        self.assertFalse(is_room_occupied(self.room1))


    def test_is_room_occupied_one_sensor_false(self):
        """
        Scenario 4: Verify that if any sensor returns False for presence_detected,
        the room should be considered unoccupied (False), even if other sensors detect presence.
        """
        RoomOccupancy.objects.create(room_name=self.room1, sensor_name=self.sensor1, presence_detected=True, temperature=22.5, timestamp=self.now - timedelta(minutes=1))
        RoomOccupancy.objects.create(room_name=self.room1, sensor_name=self.sensor2, presence_detected=False, temperature=22.5, timestamp=self.now - timedelta(minutes=1))
        self.assertFalse(is_room_occupied(self.room1))

    @freeze_time(lambda: timezone.now())
    def test_is_room_occupied_checks_last_3_minutes(self):
        """
        Scenario 5: Verify that the function only checks the last 3 minutes.
        Adding a record that is older than 3 minutes should not affect the result.
        """
        # Clear existing records for Room1
        RoomOccupancy.objects.filter(room_name=self.room1).delete()
        
        # Add a record that's older than 3 minutes with presence_detected=True
        with freeze_time(self.frozen_time - timedelta(minutes=5)):
            RoomOccupancy.objects.create(
                room_name=self.room1,
                sensor_name=self.sensor1,
                presence_detected=True,
                temperature=22.5
            )
        
        # Add a record within the last 3 minutes with presence_detected=False
        with freeze_time(self.frozen_time - timedelta(minutes=2)):
            RoomOccupancy.objects.create(
                room_name=self.room1,
                sensor_name=self.sensor2,
                presence_detected=False,
                temperature=22.5
            )
        
        # Debug: Print all records for Room1
        print("\nAll records for Room1:")
        for record in RoomOccupancy.objects.filter(room_name=self.room1):
            print(f"Room: {record.room_name}, Sensor: {record.sensor_name}, Time: {record.timestamp}, Presence: {record.presence_detected}")
        
        result = is_room_occupied(self.room1)
        print(f"\nis_room_occupied result: {result}")
        
        self.assertFalse(result)