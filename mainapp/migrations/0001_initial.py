# Generated by Django 4.2.2 on 2023-06-19 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnmDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobile_no', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AshaWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobile_no', models.CharField(max_length=255)),
                ('district_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('Age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('parent_name', models.CharField(max_length=255)),
                ('district_name', models.CharField(max_length=255)),
                ('village_name', models.CharField(max_length=255)),
                ('mobile_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VaccineCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('district_name', models.CharField(max_length=255)),
                ('village_name', models.CharField(max_length=255)),
                ('health_subcentre_name', models.CharField(max_length=255)),
                ('health_facility_name', models.CharField(max_length=255)),
                ('health_block_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VaccineDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_administered', models.DateField()),
                ('anm_worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.anmdetails')),
                ('asha_worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ashaworker')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.child')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.vaccine')),
                ('vaccine_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.vaccinecenter')),
            ],
        ),
    ]
