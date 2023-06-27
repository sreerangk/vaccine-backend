# from rest_framework import serializers

# from mainapp.models import Child, VaccinationRecord, VaccineCenter

# class VaccinewiseVaccinatedCountSerializer(serializers.Serializer):
#     vaccine = serializers.CharField(source='vaccination__vaccine_name')
#     count = serializers.IntegerField()

# class MonthwiseVaccinatedCountSerializer(serializers.Serializer):
#     year = serializers.IntegerField()
#     month = serializers.IntegerField()
#     count = serializers.IntegerField()


# class VaccinatedChildCountSerializer(serializers.Serializer):
#     child__district_name = serializers.CharField()
#     child_count = serializers.IntegerField()

    
# class VaccineCenterSerializer(serializers.ModelSerializer):
#     missed_count = serializers.SerializerMethodField()

#     def get_missed_count(self, obj):
#         missed_count = VaccinationRecord.objects.filter(vaccine_center=obj).count()
#         return missed_count

#     class Meta:
#         model = VaccineCenter
#         fields = ('village_name', 'missed_count')