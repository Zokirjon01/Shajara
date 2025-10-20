from django.db import models
from datetime import date

# Create your models here.

class Odam(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    father = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='ota_farzandlari')
    mother = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='ona_farzandlari')
    address = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='odamlar/', null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    def yosh(self):
        if self.birth_date:
            today = date.today()
            return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
            )
        return None

    def __str__(self):
        return self.full_name


    def farzandlar(self):
        return Odam.objects.filter(models.Q(father=self) | models.Q(mother=self))