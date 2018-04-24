import uuid
from django.db import models
from django.db.models import (
    UUIDField,
    CharField, 
    IntegerField,
    DateTimeField,
    ForeignKey,
)

class Doctor(models.Model):
    doctorID = UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    doctorFirstname = CharField(max_length=50, required=True)
    doctorLastname = CharField(max_length=50, required=True)
    doctorPhone = IntegerField(max_length=15)
    doctorHospital = ForeignKey(Hospital, required=False)