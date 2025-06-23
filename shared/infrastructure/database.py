

from peewee import SqliteDatabase


db = SqliteDatabase('telemetry_tracker.db')


def init_db() -> None:

    from iam.infrastructure.models import Device
    from telemetry.infrastructure.models import TelemetryRecord

    db.connect()

    db.create_tables([Device, TelemetryRecord], safe=True)

    db.close()