from dataclasses import fields
from import_export import resources
# from .models import Child,Vaccines,VaccinationRecord

# class ChildModelResource(resources.ModelResource):
#     class Meta:
#         model = Child
#         import_id_fields = []  # Disable identification of existing records
#         fields = ['child_id','child_mpid','name','age','gender','date_of_birth','parent_name','district_name','village_name','mobile_no']  
    
# class VaccinationRecordResource(resources.ModelResource):
#     class Meta:
#         model = VaccinationRecord
from datetime import datetime
from import_export import resources
from import_export.widgets import DateWidget
from .models import Child, Vaccine, VaccinationRecord
from import_export import fields

class ChildModelResource(resources.ModelResource):
    class Meta:
        model = Child
        import_id_fields = []  # Disable identification of existing records
        fields = ['child_id', 'child_mpid', 'name', 'age', 'gender', 'date_of_birth', 'parent_name', 'district_name', 'village_name', 'mobile_no']  

# class VaccinationRecordResource(resources.ModelResource):
#     vaccine_name = Field(attribute='vaccine__vaccine_name', column_name='Vaccine')
#     date_administered = Field(column_name='Date Administered', widget=DateWidget(format='%m/%d/%Y'))

#     class Meta:
#         model = VaccinationRecord
#         import_id_fields = []  # Disable identification of existing records
#         fields = ['child_id', 'anm_worker', 'vaccine', 'anm_mobile_no', 'date_administered']

#     def before_import_row(self, row, **kwargs):
#         # Extract the vaccine value from the row
#         vaccine_name = row.get('vaccine')  # Assuming the vaccine name is in a column named 'vaccine'

#         # If no matching vaccine found, create a new Vaccine object
#         if vaccine_name and not Vaccine.objects.filter(vaccine_name=vaccine_name).exists():
#             vaccine = Vaccine.objects.create(vaccine_name=vaccine_name)
#         else:
#             vaccine = Vaccine.objects.get(vaccine_name=vaccine_name)

#         # Update the row data with the corresponding Vaccine object
#         row['vaccine'] = vaccine



#     def import_row(self, row, instance_loader, **kwargs):
#         # Get the child object based on the child_id from the row
#         child_id = row.get('child_id')
#         child = Child.objects.get(child_id=child_id)

#         # Create the VaccinationRecord object
#         vaccination_record = VaccinationRecord(
#             child_id=child,
      
#             vaccine=row.get('vaccine'),
#             date_administered=row.get('date_administered')
#         )
#         vaccination_record.save()
from import_export import resources
from import_export import widgets


from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Child, Vaccine, VaccinationRecord

from import_export import resources, fields, widgets
from .models import Child, Vaccine, VaccinationRecord

# class VaccinationRecordResource(resources.ModelResource):
#     child_id = fields.Field(
#         column_name='child_id',
#         attribute='child_id',
#         widget=widgets.ForeignKeyWidget(Child, 'child_id')
#     )
#     date_administered = fields.Field(column_name='date_administered', attribute='date_administered')
#     anm_name = fields.Field(column_name='anm_name', attribute='anm_name')
#     anm_mobile_no = fields.Field(column_name='anm_mobile_no', attribute='anm_mobile_no')

#     def before_import_row(self, row, **kwargs):
#         child_id = row.get('child_id')

#         # Iterate over the vaccine columns and create vaccination records
#         for column_name in row.keys():
#             # Skip the fixed columns and columns without a date value
#             if column_name not in ['child_id', 'date_administered', 'anm_name', 'anm_mobile_no'] and row[column_name]:
#                 try:
#                     vaccine = Vaccine.objects.get(vaccine_name=column_name)
#                 except Vaccine.DoesNotExist:
#                     continue

#                 child = Child.objects.get(child_id=child_id)
#                 VaccinationRecord.objects.create(
#                     child_id=child,
#                     vaccine=vaccine,
#                     date_administered=row[column_name],
#                     anm_name=row.get('anm_name'),
#                     anm_mobile_no=row.get('anm_mobile_no')
#                 )

#     class Meta:
#         model = VaccinationRecord
#         fields = ['id','child_id', 'date_administered', 'anm_name', 'anm_mobile_no']
from import_export import resources, fields, widgets
from .models import Child, Vaccine, VaccinationRecord

class VaccinationRecordResource(resources.ModelResource):
    child_id = fields.Field(
        column_name='child_id',
        attribute='child_id',
        widget=widgets.ForeignKeyWidget(Child, 'child_id')
    )
    date_administered = fields.Field(column_name='date_administered', attribute='date_administered')
    anm_name = fields.Field(column_name='anm_name', attribute='anm_name')
    anm_mobile_no = fields.Field(column_name='anm_mobile_no', attribute='anm_mobile_no')

    # Mapping of column names to vaccine names
    COLUMN_MAPPING = {
        'bcg': 'bcg',
        'opv0': 'opv0',
        'opv1': 'opv1',
        'opv2': 'opv2',
        'opv3': 'opv3',
        'opvB':'opvB',
        'dpt1': 'dpt1',
        'dpt2': 'dpt2',
        'dpt3': 'dpt3',
        'dptB1': 'dptB1',
        'dptB2': 'dptB2',
        'hepB0': 'hepB0',
        'hepB1': 'hepB1',
        'hepB2': 'hepB2',
        'hepB3': 'hepB3',
        'pentavalentVaccine1': 'pentavalentVaccine1',
        'pentavalentVaccine2': 'pentavalentVaccine2',
        'pentavalentVaccine3': 'pentavalentVaccine3',
        'measles1': 'measles1',
        'measles2': 'measles2',
        'jevaccine1': 'jevaccine1',
        'jevaccine2': 'jevaccine2',
        'vitaminA1': 'vitaminA1',
        'vitaminA2': 'vitaminA2',
        'vitaminA3': 'vitaminA3',
        'vitaminA4': 'vitaminA4',
        'vitaminA5': 'vitaminA5',
        'vitaminA6': 'vitaminA6',
        'vitaminA7': 'vitaminA7',
        'vitaminA8': 'vitaminA8',
        'vitaminA9': 'vitaminA9',
        'mr2': 'mr2',
        'rotA1': 'rotA1',
        'rotA2': 'rotA2',
        'rotA3': 'rotA3',
        'ivp1': 'ivp1',
        'ivp2': 'ivp2',
        'albendazol': 'albendazol',
        'pcv2': 'pcv2',
        'pcvBooster': 'pcvBooster',
        'mr1': 'mr1',
        # Add more mappings as needed
    }

    def before_import_row(self, row, **kwargs):
        child_id = row.get('child_id')
        vaccines_data = {column_name: row.get(column_name) for column_name in self.COLUMN_MAPPING.keys()}

        # Check if all vaccine-related fields are empty
        if all(value in [None, 'NULL'] for value in vaccines_data.values()):
            return

        # Iterate over the column mapping and create vaccination records
        for column_name, vaccine_name in self.COLUMN_MAPPING.items():
            if vaccines_data[column_name] and vaccines_data[column_name] != 'NULL':
                try:
                    vaccine = Vaccine.objects.get(vaccine_name=vaccine_name)
                except Vaccine.DoesNotExist:
                    continue

                child = Child.objects.get(child_id=child_id)
                date_administered = row[column_name]

                # Skip saving the record if date_administered is null
                if date_administered in [None, 'NULL']:
                    continue

                # Skip saving the record if vaccine is null
                if vaccine is None:
                    continue

                VaccinationRecord.objects.create(
                    child_id=child,
                    vaccine=vaccine,
                    date_administered=date_administered,
                    anm_name=row.get('anm_name'),
                    anm_mobile_no=row.get('anm_mobile_no')
                )


    class Meta:
        model = VaccinationRecord
        fields = ['id','child_id', 'date_administered', 'anm_name', 'anm_mobile_no']
