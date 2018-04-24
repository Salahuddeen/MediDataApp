import uuid
from django.db import models
from django.db.models import (
    UUIDField,
    CharField, 
    IntegerField,
    DateTimeField,
    ForeignKey,
)

class Treatment(models.Model):
    treatmentId = UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    treatmentDescription = CharField(max_length=500)