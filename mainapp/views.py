import json
from django.http import HttpResponse, JsonResponse
from django.db.models import Count

from mainapp.serializers import DistrictPatientCountSerializer, MonthwiseVaccinatedCountSerializer, VaccinatedPatientsCountSerializer, VaccineCenterSerializer, VaccinewiseVaccinatedCountSerializer
from .models import Patient, VaccineCenter, VaccinationRecord
from django.db.models.functions import ExtractYear, ExtractMonth

from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Subquery, OuterRef, ExpressionWrapper, IntegerField
from rest_framework.views import APIView
from rest_framework.response import Response



def index(request):
    return HttpResponse("Server is up!!")

class VaccinatedPatientsCountAPIView(APIView):
    def get(self, request):
        vaccinated_count = Patient.objects.annotate(count=Count('vaccinationrecord__patient')).values('district_name', 'count')

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

from django.db.models import Count
from django.http import JsonResponse


class DistrictPatientCountAPIView(APIView):
    def get(self, request):
        district_count = Patient.objects.values('district_name').annotate(patient_count=Count('vaccinationrecord__patient', distinct=True))

        serializer = DistrictPatientCountSerializer(district_count, many=True)

        return Response(serializer.data)


class MissedVaccineCountByVillageAPIView(APIView):
    def get(self, request, format=None):
        subquery = VaccinationRecord.objects.filter(vaccine_center=OuterRef('pk')).values('vaccine_center')
        missed_vaccine_counts = VaccineCenter.objects.annotate(
            missed_count=ExpressionWrapper(
                Subquery(subquery.annotate(count=Count('patient')).values('count')[:1]),
                output_field=IntegerField()
            )
        ).exclude(missed_count=0).order_by('-missed_count')[:10]

        serializer = VaccineCenterSerializer(missed_vaccine_counts, many=True)
        return Response(serializer.data)