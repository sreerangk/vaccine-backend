from django.urls import path
from . import views
from .views import VaccinewiseVaccinatedCountAPIView, MonthwiseVaccinatedCountAPIView, VaccinatedPatientsCountAPIView
app_name = 'mainapp'

urlpatterns = [
    path('vaccinated-patients-count/', VaccinatedPatientsCountAPIView.as_view(), name='vaccinated-patients-count'),
    path('monthwise-vaccinated-count/', MonthwiseVaccinatedCountAPIView.as_view(), name='monthwise-vaccinated-count'),
    path('vaccinated-count/', VaccinewiseVaccinatedCountAPIView.as_view(), name='vaccinated-count'),

]
