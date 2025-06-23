

from datetime import datetime

class TelemetryRecord:

    def __init__(self,
                 device_id: str,
                 temperature: float,
                 humidity: float,
                 latitude: float,
                 longitude: float,
                 altitude: float,
                 speed: float,
                 recorded_at: datetime,
                 id: int = None):
        self.id = id
        self.device_id = device_id
        self.temperature = temperature
        self.humidity = humidity
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.speed = speed
        self.recorded_at = recorded_at