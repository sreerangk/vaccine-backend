# Generated by Django 4.2.2 on 2023-06-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='Age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='child_mpid',
            field=models.IntegerField(),
        ),
    ]
