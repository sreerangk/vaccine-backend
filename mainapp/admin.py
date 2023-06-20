from django.contrib import admin

from mainapp.models import AshaWorker, VaccineCenter,AnmDetails,Child,VaccinationRecord,VaccineDetails,Vaccine

# Register your models here.

admin.site.register(VaccineCenter)

class AshaWorkerAmin(admin.ModelAdmin):
    list_display = ["name","district_name","mobile_no"]
    
admin.site.register(AshaWorker, AshaWorkerAmin)
class AnmDetailsAdmin(admin.ModelAdmin):
    list_display = ["name","mobile_no"] 
admin.site.register(AnmDetails)

class ChildAdmin(admin.ModelAdmin):
    list_display = ["name","district_name",]
   
admin.site.register(Child,ChildAdmin)

  
admin.site.register(VaccinationRecord)
admin.site.register(VaccineDetails)

class VaccineAdmin(admin.ModelAdmin):
    list_display = ['vaccine_name']
    
    def __str__(self):
        return self.vaccine_name
admin.site.register(Vaccine, VaccineAdmin)