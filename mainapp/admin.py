from django.contrib import admin

from mainapp.models import AshaWorker, VaccineCenter,AnmDetails,Child,VaccinationRecord,VaccineDetails,Vaccine
from import_export.admin import ImportExportModelAdmin

from .resources import childmodel,VaccinationRecordResource
# Register your models here.

admin.site.register(VaccineCenter)

class AshaWorkerAmin(admin.ModelAdmin):
    list_display = ["name","district_name","mobile_no"]
    
admin.site.register(AshaWorker, AshaWorkerAmin)
class AnmDetailsAdmin(admin.ModelAdmin):
    list_display = ["name","mobile_no"] 
admin.site.register(AnmDetails)

# class ChildAdmin(admin.ModelAdmin):
#     list_display = ["name","district_name",]
   
# admin.site.register(Child,ChildAdmin)

  
# admin.site.register(VaccinationRecord)
admin.site.register(VaccineDetails)

class VaccineAdmin(admin.ModelAdmin):
    list_display = ['vaccine_name']
    
    def __str__(self):
        return self.vaccine_name
admin.site.register(Vaccine, VaccineAdmin)


@admin.register(Child)
class ChildAdmin(ImportExportModelAdmin):
    list_display = ["name","child_mpid",]
    resource_class = childmodel
    

@admin.register(VaccinationRecord)
class VaccinationRecordmodel(ImportExportModelAdmin):
    list_display =["child"]
    resource_classes = (VaccinationRecordResource,)