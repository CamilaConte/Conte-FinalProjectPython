# Generated by Django 5.0.6 on 2024-07-04 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_extrauserdata_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrauserdata',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
