import uuid
from django.db import models
from django.db.models import (
    UUIDField,
    CharField, 
    IntegerField,
    DateTimeField,
    ForeignKey,
)
from ..doctor import Doctor
from ..patient import Patient
from ..treatment import Treatment
class Appointment(models.Model):
    patient = ForeignKey(Patient, on_delete='CASCADE')
    doctor = ForeignKey(Doctor, on_delete='CASCADE')
    appointmentDate = DateTimeField()
    reasonForVisiting = CharField(max_length=500)
    symptoms = CharField(max_length=500)
    treatment = ForeignKey(Treatment, on_delete='CASCADE')