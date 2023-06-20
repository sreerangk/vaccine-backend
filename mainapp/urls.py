from django.urls import path
from . import views
from .views import VaccineStatusAPIView,MissedVaccineCountByVillageAPIView, VaccinewiseVaccinatedCountAPIView, MonthwiseVaccinatedCountAPIView, VaccinatedChildCountAPIView
app_name = 'mainapp'

urlpatterns = [
    path("", views.index, name="index"),
    path('vaccinated-child-count/', VaccinatedChildCountAPIView.as_view(), name='vaccinated-child-count'),
    path('monthwise-vaccinated-count/', MonthwiseVaccinatedCountAPIView.as_view(), name='monthwise-vaccinated-count'),
    path('vaccinated-count/', VaccinewiseVaccinatedCountAPIView.as_view(), name='vaccinated-count'),
    path('missvaccinated',MissedVaccineCountByVillageAPIView.as_view(), name="vaccinated"),
    path('vaccinestatus',VaccineStatusAPIView.as_view(), name="vaccinestatus"),
]
