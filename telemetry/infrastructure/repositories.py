
from telemetry.domain.entities import TelemetryRecord
from telemetry.infrastructure.models import TelemetryRecord as TelemetryRecordModel


class TelemetryRecordRepository:

    @staticmethod
    def save(record: TelemetryRecord) -> TelemetryRecord:

        db_record = TelemetryRecordModel.create(
            device_id=record.device_id,
            temperature=record.temperature,
            humidity=record.humidity,
            latitude=record.latitude,
            longitude=record.longitude,
            altitude=record.altitude,
            speed=record.speed,
            recorded_at=record.recorded_at
        )


        record.id = db_record.id

        return record