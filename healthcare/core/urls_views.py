from django.urls import path
from .views import (
    register_view, login_view, logout_view,
    patient_list, patient_detail, patient_create, patient_update, patient_delete,
    doctor_list, doctor_detail, doctor_create, doctor_update, doctor_delete,
    mapping_list, mapping_create, mapping_delete
)

urlpatterns = [
    # Authentication
    path('auth/register/', register_view, name='register'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),
    
    # Patients
    path('patients/', patient_list, name='patient-list'),
    path('patients/<int:pk>/', patient_detail, name='patient-detail'),
    path('patients/create/', patient_create, name='patient-create'),
    path('patients/<int:pk>/update/', patient_update, name='patient-update'),
    path('patients/<int:pk>/delete/', patient_delete, name='patient-delete'),
    
    # Doctors
    path('doctors/', doctor_list, name='doctor-list'),
    path('doctors/<int:pk>/', doctor_detail, name='doctor-detail'),
    path('doctors/create/', doctor_create, name='doctor-create'),
    path('doctors/<int:pk>/update/', doctor_update, name='doctor-update'),
    path('doctors/<int:pk>/delete/', doctor_delete, name='doctor-delete'),
    
    # Mappings
    path('mappings/', mapping_list, name='mapping-list'),
    path('mappings/create/', mapping_create, name='mapping-create'),
    path('mappings/<int:pk>/delete/', mapping_delete, name='mapping-delete'),
]