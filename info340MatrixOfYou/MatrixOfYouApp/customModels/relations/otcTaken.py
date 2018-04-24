import uuid
from django.db import models
from django.db.models import (
    UUIDField,
    CharField, 
    IntegerField,
    DateTimeField,
    ForeignKey,
)
from ..otcMedication import OTCMedicine
from ..patient import Patient

class OTCMeds(models.Model):
    patient = ForeignKey(Patient, on_delete='CASCADE')
    medicine = ForeignKey(OTCMedicine, on_delete='CASCADE')

    DAILY = "DD"
    TEMPORARY = "TP"
    MEDS_CHOICE = (
        (DAILY, "Daily"),
        (TEMPORARY, "Temporary")
    )
    
    intakeFrequency = CharField(
        max_length=2,
        choices=MEDS_CHOICE,
        default=DAILY,
    )