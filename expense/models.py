from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ExpensesCategory(models.Model):
    title  = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Expenses(models.Model):
    title = models.CharField(max_length=100)
    cost = models.FloatField()
    description = models.TextField(null=True,blank=True)
    bill = models.FileField(upload_to='billing/')
    category = models.ForeignKey(ExpensesCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
