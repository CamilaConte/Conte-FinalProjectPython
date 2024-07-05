from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document = models.IntegerField()
    phone_number = models.IntegerField()
    birth_date = models.DateField()
    last_xray = models.ImageField(upload_to='xrays', blank=True, null=True)
    observations = models.TextField()
    # TODO: agregar campo de imagen como "ultima radiogradia" o similar para poner en el header
    
    def __str__(self):
        return f"{self.last_name}, {self.name}. Document: {self.document}."
    
