from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class IncomeCategory(models.Model):
    title = models.CharField(max_length=100)
    user= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Income(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    rupes = models.FloatField()
    category = models.ForeignKey(IncomeCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


