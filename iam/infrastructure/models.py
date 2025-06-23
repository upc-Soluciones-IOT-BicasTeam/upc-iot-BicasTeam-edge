# iam/infrastructure/models.py


from peewee import Model, CharField, DateTimeField
from shared.infrastructure.database import db # Import the shared database connection

class Device(Model):

    device_id   = CharField(primary_key=True, max_length=50)
    api_key     = CharField(max_length=100)
    created_at  = DateTimeField()

    class Meta:
        database    = db
        table_name  = 'devices'