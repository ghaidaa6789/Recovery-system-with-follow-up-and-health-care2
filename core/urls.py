from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, MedicalRecordViewSet, MedicalReportViewSet,SpecialtyViewSet,DepartmentViewSet, AppointmentViewSet,VitalSignViewSet,MedicalAlertViewSet, MedicationViewSet,LabRequestViewSet


router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'medical-records', MedicalRecordViewSet)
router.register(r'medical-reports', MedicalReportViewSet)
router.register(r'specialties', SpecialtyViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'vital-signs', VitalSignViewSet)
router.register(r'medical-alerts', MedicalAlertViewSet)
router.register(r'medications', MedicationViewSet)
router.register(r'lab-requests', LabRequestViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

