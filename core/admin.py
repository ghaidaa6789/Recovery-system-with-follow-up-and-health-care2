from django.contrib import admin
from .models import Patient, Appointment, Department, Specialty, MedicalRecord, MedicalReport, Medication, MedicalAlert, LabRequest, VitalSign

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Department)
admin.site.register(Specialty)
admin.site.register(MedicalRecord)
admin.site.register(MedicalReport)
admin.site.register(Medication)
admin.site.register(MedicalAlert)
admin.site.register(LabRequest)
admin.site.register(VitalSign)
