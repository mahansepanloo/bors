from django.db import models
from django.contrib.auth.models import User

class Nameasset(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Namemonth(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class PriceChange(models.Model):
    fund = models.ForeignKey(Nameasset, on_delete=models.CASCADE)
    month = models.ForeignKey(Namemonth, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.fund.name} - {self.month}: {self.price}"




class Investment(models.Model):
    investor = models.ForeignKey(User, on_delete=models.CASCADE)
    fund = models.ForeignKey(PriceChange, on_delete=models.CASCADE)
    initial_amount = models.IntegerField()
    start_month = models.CharField(max_length=20)
    end_month = models.CharField(max_length=20)
    profit = models.FloatField(null=True,blank=True)
    def __str__(self):
        return self.investor.username