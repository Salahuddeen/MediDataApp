import uuid
from random import *
from django.db import models
from django.db.models import (
    UUIDField,
    CharField, 
    IntegerField,
    DateTimeField,
    ForeignKey,
)

class Patient(models.Model):
    randomNum = "%05d" % randint(0,99999)
    patientID = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patientFirstname = CharField(max_length=50, required=True)
    patientLastname = CharField(max_length=50, required=True)
    patientAddress = CharField(max_length=200, required=True)
    patientPhone = IntegerField(max_length=15, required=True)
    patientAlternateName = CharField(max_length=200 required=False)
    patientAlternateContact = CharField(max_length=15, required=False)
    patientViewCode = CharField(max_length=5, required=True, default=randomNum)

    class Meta:
        ordering = ('patientLastname', 'patientFirstname')
