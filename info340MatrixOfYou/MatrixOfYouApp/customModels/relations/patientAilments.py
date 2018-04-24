import uuid
from django.db import models
from django.db.models import (
    UUIDField,
    CharField, 
    IntegerField,
    DateTimeField,
    ForeignKey,
)
from ..ailments import Ailments
from ..patient import Patient

class patientIllness(models.Model):
    patient = ForeignKey(Patient, on_delete='CASCADE')
    ailment = ForeignKey(Ailments, on_delete='CASCADE')
    dateDiagnosed = DateTimeField(auto_now_add=True)
    dateCured = DateTimeField(blank=True, null=True)
