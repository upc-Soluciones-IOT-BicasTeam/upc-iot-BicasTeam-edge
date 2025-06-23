

from datetime import datetime, timezone
from dateutil.parser import parse
from telemetry.domain.entities import TelemetryRecord

class TelemetryRecordService:

    @staticmethod
    def create_record(device_id: str, temp: float, hum: float, lat: float, lon: float,
                      alt: float, spd: float, timestamp: str | None) -> TelemetryRecord:

        try:
            temp = float(temp)
            hum = float(hum)
            lat = float(lat)
            lon = float(lon)
            alt = float(alt)
            spd = float(spd)
        except (ValueError, TypeError):
            raise ValueError("Invalid data format: temperature, humidity, and GPS data must be numbers.")

        if not (-50 <= temp <= 100):
            raise ValueError(f"Invalid temperature value: {temp}. Must be between -50 and 100°C.")
        if not (0 <= hum <= 100):
            raise ValueError(f"Invalid humidity value: {hum}. Must be between 0 and 100%.")
        if not (-90 <= lat <= 90):
            raise ValueError(f"Invalid latitude: {lat}. Must be between -90 and 90.")
        if not (-180 <= lon <= 180):
            raise ValueError(f"Invalid longitude: {lon}. Must be between -180 and 180.")
        if spd < 0:
            raise ValueError(f"Speed cannot be negative: {spd}.")

        try:
            if timestamp:
                parsed_recorded_at = parse(timestamp).astimezone(timezone.utc)
            else:
                parsed_recorded_at = datetime.now(timezone.utc)
        except (ValueError, TypeError):
            raise ValueError("Invalid timestamp format. Expected ISO 8601 string (e.g., 'YYYY-MM-DDTHH:MM:SSZ').")

        return TelemetryRecord(
            device_id=device_id, temperature=temp, humidity=hum, latitude=lat,
            longitude=lon, altitude=alt, speed=spd, recorded_at=parsed_recorded_at
        )