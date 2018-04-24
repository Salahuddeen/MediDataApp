import uuid
from django.db import models
from django.db.models import (
    UUIDField,
    CharField, 
    IntegerField,
    DateTimeField,
    ForeignKey,
)
from .hospital import Hospital

class Doctor(models.Model):
    doctorID = UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    doctorFirstname = CharField(max_length=50)
    doctorLastname = CharField(max_length=50)
    doctorPhone = IntegerField()
    doctorHospital = ForeignKey(Hospital, blank=True, null=True, on_delete='CASCADE')