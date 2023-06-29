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
from import_export import resources
from tablib import Dataset

from .models import Vaccine, VaccinationRecord, Child
class VaccinationRecordResource(resources.ModelResource):
    class Meta:
        model = VaccinationRecord
        skip_unchanged = True
        report_skipped = False
        

    def before_import_row(self, row, **kwargs):
        child_id = row['child_id']  # Modify according to your column name in the import file
        child = Child.objects.get(child_id=child_id)

        # Iterate over the columns dynamically
        for column_name, value in row.items():
            # Skip if the value is NULL or empty
            if value is None or value == 'NULL' or value == '':
                continue
                
            # Check if the column corresponds to a vaccine name
            try:
                vaccine = Vaccine.objects.get(vaccine_name=column_name)
                date_administered = value
                anm_name = row.get('anm_name')  # Modify according to your column name in the import file
                anm_mobile_no = row.get('anm_mobile_no')  # Modify according to your column name in the import file
                asha_mobile = row.get('asha_mobile')
                asha_worker = row.get('asha_worker')
                # Create a new VaccinationRecord instance with the data
                vaccination_record = VaccinationRecord(
                    child_id=child,
                    vaccine=vaccine,
                    date_administered=date_administered,
                    anm_name=anm_name,
                    anm_mobile_no=anm_mobile_no,
                    asha_mobile=asha_mobile,
                    asha_worker=asha_worker,
                )

                # Save the VaccinationRecord instance
                vaccination_record.save()

            except Vaccine.DoesNotExist:
                continue

    def after_import(self, dataset: Dataset, result, using_transactions, dry_run, **kwargs):
        imported_data = dataset.dict  # Convert the dataset to a dictionary

        # Get the vaccine names from the Vaccine table
        vaccine_names = set(Vaccine.objects.values_list('vaccine_name', flat=True))

        # Get the imported child_ids
        imported_child_ids = {row['child_id'] for row in imported_data if 'child_id' in row}

        # Query the VaccinationRecord objects to delete
        invalid_records = VaccinationRecord.objects.exclude(vaccine__vaccine_name__in=vaccine_names) \
            .filter(child_id__in=imported_child_ids)

        # Delete the invalid VaccinationRecord objects
        invalid_records.delete()
