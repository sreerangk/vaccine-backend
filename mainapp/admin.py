from django.contrib import admin

from mainapp.models import Child,VaccinationRecord,Vaccine
from import_export.admin import ImportExportModelAdmin

from .resources import ChildModelResource,VaccinationRecordResource
# Register your models here.

# admin.site.register(VaccineCenter)

# class AshaWorkerAmin(admin.ModelAdmin):
#     list_display = ["name","district_name","mobile_no"]
    
# admin.site.register(AshaWorker, AshaWorkerAmin)
# class AnmDetailsAdmin(admin.ModelAdmin):
#     list_display = ["name","mobile_no"] 
# admin.site.register(AnmDetails)

# class ChildAdmin(admin.ModelAdmin):
#     list_display = ["name","district_name",]
   
# admin.site.register(Child,ChildAdmin)

  
# admin.site.register(VaccinationRecord)
# admin.site.register(VaccineDetails)

class VaccineAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.vaccine_name
admin.site.register(Vaccine, VaccineAdmin)


@admin.register(Child)
class ChildAdmin(ImportExportModelAdmin):
    resource_class = ChildModelResource
    

@admin.register(VaccinationRecord)
class VaccinationRecordmodel(ImportExportModelAdmin):
    resource_classes = (VaccinationRecordResource,)