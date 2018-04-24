import uuid
from django.db import models
from django.db.models import (
    UUIDField,
    CharField, 
    IntegerField,
    DateTimeField,
    ForeignKey,
)

class OTCMedicine(models.Model):
    medicineID = UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    medicineName = CharField(max_length=100, required=True)
    medicineUse = CharField(max_length=100, required=True)