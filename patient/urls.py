from django.urls import path

from . import views


urlpatterns = [
    path('create-patient/', views.create_patient, name='create_patient'),
    path('get-all-patients/', views.get_all_patients, name='get_all_patients'),
    path('get-patient-by-id/<int:id>/', views.get_patient_by_id, name='get_patient_by_id'),
    path('update-patient/<int:id>/', views.update_patient, name='update_patient'),
    path('delete-patient/<int:id>/', views.delete_patient, name='delete_patient')
]