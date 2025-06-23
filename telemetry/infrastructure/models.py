
from peewee import Model, AutoField, FloatField, CharField, DateTimeField
from shared.infrastructure.database import db # Import the shared database connection

class TelemetryRecord(Model):

    id = AutoField()  # Primary key, automatically increments.
    device_id = CharField()
    temperature = FloatField()
    humidity = FloatField()
    latitude = FloatField()
    longitude = FloatField()
    altitude = FloatField()
    speed = FloatField()
    recorded_at = DateTimeField()

    class Meta:

        database = db
        table_name = 'telemetry_records'