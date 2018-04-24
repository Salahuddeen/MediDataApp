import uuid
from django.db import models
from django.db.models import (
    UUIDField,
    CharField, 
    IntegerField,
    DateTimeField,
    ForeignKey,
)

class Ailments(models.Model):
    ailmentID = UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    ailmentDesc = CharField(max_length=100)
    additionalInfo = CharField(max_length=100, blank=True, null=True)