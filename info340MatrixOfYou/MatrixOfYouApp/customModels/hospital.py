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
    hospitalName = CharField(max_length=100)
    hospitalAddress = CharField(max_length=400)
    hospitalPhone = IntegerField()