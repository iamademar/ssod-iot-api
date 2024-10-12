import os
from Adafruit_IO import Client, Feed, RequestError

class AdafruitService:
    def __init__(self):
        self.username = os.environ.get('ADAFRUIT_IO_USERNAME')
        self.key = os.environ.get('ADAFRUIT_IO_KEY')
        self.client = Client(self.username, self.key)
        self.feeds = {
            'WZ321': 'room-occupancy-wz321',
            'WZ320': 'room-occupancy-wz320'
        }
        self._ensure_feeds_exist()

    def _ensure_feeds_exist(self):
        for room, feed_key in self.feeds.items():
            try:
                self.client.feeds(feed_key)
            except RequestError:
                self.client.create_feed(Feed(name=feed_key))

    def publish_occupancy(self, room_name, presence_detected):
        if room_name in self.feeds:
            feed_key = self.feeds[room_name]
            try:
                # Only send 'true' if presence is detected
                if presence_detected:
                    self.client.send(feed_key, 'true')
                    print(f"Presence detected in {room_name}. Sent 'true' to Adafruit IO feed {feed_key}")
                else:
                    print(f"No presence detected in {room_name}. No data sent to Adafruit IO.")
            except RequestError as e:
                print(f"Failed to send data to Adafruit IO feed {feed_key}: {e}")
        else:
            print(f"No Adafruit IO feed configured for room {room_name}")

adafruit_service = AdafruitService()