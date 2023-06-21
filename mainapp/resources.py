from import_export import resources
from .models import Child,VaccinationRecord

class childmodel(resources.ModelResource):
    class Meta:
        model = Child
    
class VaccinationRecordResource(resources.ModelResource):
    class Meta:
        model = VaccinationRecord