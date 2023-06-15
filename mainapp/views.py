import json
from django.http import JsonResponse
from django.db.models import Count

from mainapp.serializers import MonthwiseVaccinatedCountSerializer, VaccinatedPatientsCountSerializer, VaccinewiseVaccinatedCountSerializer
from .models import VaccineCenter, VaccinationRecord
from django.db.models.functions import ExtractYear, ExtractMonth
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

class VaccinatedPatientsCountAPIView(APIView):
    def get(self, request):
        vaccinated_count = VaccineCenter.objects.annotate(count=Count('vaccinationrecord__patient')).values('district_name', 'count')

        serializer = VaccinatedPatientsCountSerializer(vaccinated_count, many=True)

        return Response(serializer.data)

class MonthwiseVaccinatedCountAPIView(APIView):
    def get(self, request):
        vaccinated_count = VaccinationRecord.objects.annotate(year=ExtractYear('date_administered'), month=ExtractMonth('date_administered')).values('year', 'month').annotate(count=Count('id'))

        serializer = MonthwiseVaccinatedCountSerializer(vaccinated_count, many=True)

        return Response(serializer.data)

class VaccinewiseVaccinatedCountAPIView(APIView):
    def get(self, request):
        vaccinated_count = VaccinationRecord.objects.values('vaccination__vaccine_name').annotate(count=Count('id'))

        serializer = VaccinewiseVaccinatedCountSerializer(vaccinated_count, many=True)

        return Response(serializer.data)
