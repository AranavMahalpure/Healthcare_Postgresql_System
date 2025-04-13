from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import (
    UserRegistrationAPIView,
    PatientListCreateAPIView, PatientRetrieveUpdateDestroyAPIView,
    DoctorListCreateAPIView, DoctorRetrieveUpdateDestroyAPIView,
    PatientDoctorMappingListCreateAPIView, PatientDoctorMappingRetrieveDestroyAPIView,
    PatientDoctorsListAPIView
)

urlpatterns = [
    # Authentication
    path('auth/register/', UserRegistrationAPIView.as_view(), name='api-register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='api-login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='api-refresh'),
    
    # Patients
    path('patients/', PatientListCreateAPIView.as_view(), name='api-patient-list'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyAPIView.as_view(), name='api-patient-detail'),
    
    # Doctors
    path('doctors/', DoctorListCreateAPIView.as_view(), name='api-doctor-list'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyAPIView.as_view(), name='api-doctor-detail'),
    
    # Mappings
    path('mappings/', PatientDoctorMappingListCreateAPIView.as_view(), name='api-mapping-list'),
    path('mappings/<int:pk>/', PatientDoctorMappingRetrieveDestroyAPIView.as_view(), name='api-mapping-detail'),
    path('mappings/patient/<int:patient_id>/', PatientDoctorsListAPIView.as_view(), name='api-patient-doctors'),
]