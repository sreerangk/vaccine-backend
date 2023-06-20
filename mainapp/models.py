from django.db import models

class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.vaccine_name

class VaccineCenter(models.Model):
    name = models.CharField(max_length=255)
    district_name = models.CharField(max_length=255)
    village_name = models.CharField(max_length=255)
    health_subcentre_name = models.CharField(max_length=255)
    health_facility_name = models.CharField(max_length=255)
    health_block_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AshaWorker(models.Model):
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=255)
    district_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AnmDetails(models.Model):
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=255)
    Age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    parent_name = models.CharField(max_length=255)
    district_name = models.CharField(max_length=255)
    village_name = models.CharField(max_length=255)
    mobile_no = models.IntegerField()

    def __str__(self):
        return self.name


class VaccinationRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    asha_worker = models.ForeignKey(AshaWorker, on_delete=models.CASCADE)
    anm_worker = models.ForeignKey(AnmDetails, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    vaccine_center = models.ForeignKey(VaccineCenter, on_delete=models.CASCADE)

    date_administered = models.DateField()

    def __str__(self):
        return f"{self.child} - {self.vaccine}"



class VaccineDetails(models.Model):
    descriptions = models.CharField(max_length=255)
