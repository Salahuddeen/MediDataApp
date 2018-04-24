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
    patientFirstname = CharField(max_length=50)
    patientLastname = CharField(max_length=50)
    patientAddress = CharField(max_length=200)
    patientPhone = IntegerField()
    patientAlternateName = CharField(max_length=200, blank=True, null=True)
    patientAlternateContact = CharField(max_length=15, blank=True, null=True)
    patientViewCode = CharField(max_length=5, default=randomNum)

    class Meta:
        ordering = ('patientLastname', 'patientFirstname')
