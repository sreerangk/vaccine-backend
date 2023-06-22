from import_export import resources
from .models import Child,VaccinationRecord

class ChildModelResource(resources.ModelResource):
    class Meta:
        model = Child
        import_id_fields = []  # Disable identification of existing records
        fields = ['child_mpid','name','age','gender','date_of_birth','parent_name','district_name','village_name','mobile_no']  
    
class VaccinationRecordResource(resources.ModelResource):
    class Meta:
        model = VaccinationRecord