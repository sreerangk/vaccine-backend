from rest_framework import serializers

class VaccinewiseVaccinatedCountSerializer(serializers.Serializer):
    vaccine = serializers.CharField(source='vaccination__vaccine_name')
    count = serializers.IntegerField()

class MonthwiseVaccinatedCountSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    count = serializers.IntegerField()
    
class VaccinatedPatientsCountSerializer(serializers.Serializer):
    district_name = serializers.CharField()
    count = serializers.IntegerField()