import uuid
from django.db import models
from django.db.models import (
    UUIDField,
    CharField, 
    IntegerField,
    DateTimeField,
    ForeignKey,
)

class Hospital(models.Model):
    hospitalID = UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    hospitalName = CharField(max_length=100, required=True)
    hospitalAddress = CharField(max_length=400, required=True)
    hospitalPhone = IntegerField(max_length=15, required=True)