from django.db import models
from django.utils import timezone


# Create your models from django.db import models
class Patient(models.Model):
    full_name = models.CharField(max_length=100)  # تأكد أن هذا الحقل موجود
    birth_date = models.DateField(default='2000-01-01')
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.full_name  # أو يمكن أن يكون 'full_name' هو الحقل الذي يعرضه

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_records")
    diagnosis = models.TextField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)  # لأرشفة السجل بدل الحذف

    def __str__(self):
        return f"سجل {self.patient.full_name} بتاريخ {self.created_at.date()}"


class MedicalReport(models.Model):
    record = models.ForeignKey('MedicalRecord', on_delete=models.CASCADE, related_name='reports')
    title = models.CharField(max_length=100)
    content = models.TextField(default="غير محدد")
    report_date = models.DateField()
    doctor_name = models.CharField(max_length=100)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.report_date}"


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    staff_count = models.IntegerField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateTimeField()
    doctor_name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient} - {self.date} مع {self.doctor_name}"


class VitalSign(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="vitals")
    type = models.CharField(max_length=50)  # مثل: ضغط دم، حرارة، سكر
    value = models.FloatField()
    unit = models.CharField(max_length=20, blank=True, null=True)  # مثل: mmHg، °C
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.type}: {self.value} {self.unit}"


class MedicalAlert(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="alerts")
    message = models.CharField(max_length=255)
    alert_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"تنبيه لـ {self.patient} - {self.alert_time.strftime('%Y-%m-%d %H:%M')}"


class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medications")
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    instructions = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.patient}"


class LabRequest(models.Model):
    REQUEST_TYPES = (
        ('تحليل', 'تحليل'),
        ('أشعة', 'أشعة'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="lab_requests")
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    request_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50, default='قيد التنفيذ')

    def __str__(self):
        return f"{self.patient} - {self.request_type} - {self.status}"
