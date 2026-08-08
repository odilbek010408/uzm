from django.db import models

# Create your models here.
class Product(models.Model):
    rasm = models.ImageField(upload_to='media/')
    nomi = models.CharField(max_length=50)
    narxi = models.IntegerField()
    skidka = models.IntegerField()
    rate = models.FloatField(null=True)
    is_aksiya = models.BooleanField(default=False)
    is_arzonlashdi = models.BooleanField(default=False)
    tavsif = models.TextField(null=True)
    def __str__(self):
        return self.nomi