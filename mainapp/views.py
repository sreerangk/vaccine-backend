import json
from django.http import HttpResponse
from django.db.models import Count

from mainapp.serializers import  MonthwiseVaccinatedCountSerializer, VaccinatedChildCountSerializer, VaccineCenterSerializer, VaccinewiseVaccinatedCountSerializer
from .models import Child, VaccineCenter, VaccinationRecord
from django.db.models.functions import ExtractYear, ExtractMonth

from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Subquery, OuterRef, ExpressionWrapper, IntegerField
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Count, FloatField, Q
from django.db.models.functions import Cast

def index(request):
    return HttpResponse("Server is up!!")



class VaccinatedChildCountAPIView(APIView):
    def get(self, request):
        vaccinated_count = VaccinationRecord.objects.values('child__district_name').annotate(child_count=Count('child', distinct=True))

        serializer = VaccinatedChildCountSerializer(vaccinated_count, many=True)

        return Response(serializer.data)



class MonthwiseVaccinatedCountAPIView(APIView):
    def get(self, request):
        vaccinated_count = VaccinationRecord.objects.annotate(
            year=ExtractYear('date_administered'),
            month=ExtractMonth('date_administered')
        ).values('year', 'month').annotate(count=Count('child', distinct=True))

        serializer = MonthwiseVaccinatedCountSerializer(vaccinated_count, many=True)

        return Response(serializer.data)


class VaccinewiseVaccinatedCountAPIView(APIView):
    def get(self, request):
        vaccinated_count = VaccinationRecord.objects.values('vaccine__vaccine_name').annotate(count=Count('child', distinct=True))

        total_count = VaccinationRecord.objects.aggregate(total_count=Count('child', distinct=True))

        response_data = {
            'vaccine_count': vaccinated_count,
            'total_count': total_count['total_count']
        }

        return Response(response_data)



class MissedVaccineCountByVillageAPIView(APIView):
    def get(self, request, format=None):
        subquery = VaccinationRecord.objects.filter(vaccine_center=OuterRef('pk')).values('vaccine_center')
        missed_vaccine_counts = VaccineCenter.objects.annotate(
            missed_count=ExpressionWrapper(
                Subquery(subquery.annotate(count=Count('child')).values('count')[:1]),
                output_field=IntegerField()
            )
        ).exclude(missed_count=0).order_by('-missed_count')[:10]

        serializer = VaccineCenterSerializer(missed_vaccine_counts, many=True)
        return Response(serializer.data)

class VaccineStatusAPIView(APIView):
    def get(self, request):
        vaccinated_data = Child.objects.values('gender', 'district_name').annotate(
            total_count=Count('id', distinct=True),
            vaccinated_count=Count('id', filter=Q(vaccinationrecord__isnull=False), distinct=True),
            vaccination_percentage=Cast(Count('id', filter=Q(vaccinationrecord__isnull=False), distinct=True), FloatField()) / Cast(Count('id', distinct=True), FloatField()) * 100
        )

        return Response(vaccinated_data)