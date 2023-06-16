from django.urls import path
from . import views
from .views import DistrictPatientCountAPIView,MissedVaccineCountByVillageAPIView, VaccinewiseVaccinatedCountAPIView, MonthwiseVaccinatedCountAPIView, VaccinatedPatientsCountAPIView
app_name = 'mainapp'

urlpatterns = [
    path("", views.index, name="index"),
    path('vaccinated-patients-count/', VaccinatedPatientsCountAPIView.as_view(), name='vaccinated-patients-count'),
    path('monthwise-vaccinated-count/', MonthwiseVaccinatedCountAPIView.as_view(), name='monthwise-vaccinated-count'),
    path('vaccinated-count/', VaccinewiseVaccinatedCountAPIView.as_view(), name='vaccinated-count'),
    path('vaccinated-Distr-count/', DistrictPatientCountAPIView.as_view(), name='vaccinated-patients-count'),
    path('vaccinated',MissedVaccineCountByVillageAPIView.as_view(), name="vaccinated"),
]
