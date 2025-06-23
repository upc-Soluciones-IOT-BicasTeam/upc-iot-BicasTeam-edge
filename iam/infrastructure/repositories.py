# iam/infrastructure/repositories.py


from typing import Optional
import peewee
from datetime import datetime, timezone
from iam.domain.entities import Device
from iam.infrastructure.models import Device as DeviceModel


class DeviceRepository:

    @staticmethod
    def find_by_id_and_api_key(device_id: str, api_key: str) -> Optional[Device]:

        try:
            device_model = DeviceModel.get(
                (DeviceModel.device_id == device_id) & (DeviceModel.api_key == api_key)
            )
            return Device(device_model.device_id, device_model.api_key, device_model.created_at)
        except peewee.DoesNotExist:
            return None

    @staticmethod
    def get_or_create_test_device() -> Device:


        device_model, created = DeviceModel.get_or_create(
            device_id="ESP32_Tracker_01",
            defaults={
                "api_key": "super-secret-key-123",
                "created_at": datetime.now(timezone.utc)
            }
        )
        if created:
            print(f"Test device '{device_model.device_id}' created.")

        return Device(device_model.device_id, device_model.api_key, device_model.created_at)