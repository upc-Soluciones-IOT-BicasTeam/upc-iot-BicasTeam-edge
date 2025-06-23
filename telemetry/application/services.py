

from telemetry.domain.entities import TelemetryRecord
from telemetry.domain.services import TelemetryRecordService
from telemetry.infrastructure.repositories import TelemetryRecordRepository
from iam.application.services import AuthApplicationService  # Dependency from another context


class TelemetryRecordApplicationService:

    def __init__(self):
        self.record_repository = TelemetryRecordRepository()
        self.record_service = TelemetryRecordService()
        self.iam_service = AuthApplicationService()  # Service for authentication

    def create_telemetry_record(self, api_key: str, device_id: str, temp: float, hum: float,
                                lat: float, lon: float, alt: float, spd: float,
                                timestamp: str) -> TelemetryRecord:

        if not self.iam_service.authenticate(device_id, api_key):
            raise ValueError("Authentication failed: Invalid device_id or API key.")


        record_entity = self.record_service.create_record(
            device_id, temp, hum, lat, lon, alt, spd, timestamp
        )

        return self.record_repository.save(record_entity)