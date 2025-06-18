from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


from .models import MedicalRecord
from .serializers import MedicalRecordSerializer
from rest_framework import viewsets

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.filter(is_archived=False).order_by('-created_at')
    serializer_class = MedicalRecordSerializer

from .models import MedicalReport
from .serializers import MedicalReportSerializer

class MedicalReportViewSet(viewsets.ModelViewSet):
    queryset = MedicalReport.objects.filter(is_archived=False)
    serializer_class = MedicalReportSerializer
from .models import Specialty
from .serializers import SpecialtySerializer

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
from .models import Department
from .serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('date')
    serializer_class = AppointmentSerializer
from .models import VitalSign
from .serializers import VitalSignSerializer

class VitalSignViewSet(viewsets.ModelViewSet):
    queryset = VitalSign.objects.all().order_by('-recorded_at')
    serializer_class = VitalSignSerializer
from .models import MedicalAlert
from .serializers import MedicalAlertSerializer

class MedicalAlertViewSet(viewsets.ModelViewSet):
    queryset = MedicalAlert.objects.all().order_by('alert_time')
    serializer_class = MedicalAlertSerializer
from .models import Medication
from .serializers import MedicationSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
from .models import LabRequest
from .serializers import LabRequestSerializer

class LabRequestViewSet(viewsets.ModelViewSet):
    queryset = LabRequest.objects.all().order_by('-request_date')
    serializer_class = LabRequestSerializer