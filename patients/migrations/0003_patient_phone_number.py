# Generated by Django 5.0.6 on 2024-06-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_patient_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
    ]
