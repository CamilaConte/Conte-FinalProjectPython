from django.urls import path
from patients import views

urlpatterns = [
    path("", views.Patients.as_view(), name="patients"),
    path("create/", views.CreatePatient.as_view(), name="create_patient"),
    path("<int:pk>/", views.PatientDetail.as_view(), name="patient_detail"),
    path("<int:pk>/update/", views.UpdatePatient.as_view(), name="update_patient"),
    path("<int:pk>/delete/", views.DeletePatient.as_view(), name="delete_patient"),
]
