from django.contrib import admin

# Register your models here.
from .customModels import (
    Ailments,
    Doctor,
    Hospital,
    OTCMedicine,
    Patient,
    Treatment
)

admin.site.register(Ailments)
admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(OTCMedicine)
admin.site.register(Patient)
admin.site.register(Treatment)