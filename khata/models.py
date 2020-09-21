from django.db import models
from shop.models import Shop
import datetime
from django.shortcuts import reverse
# class Give(models.Model):
#     description = models.TextField(max_length=300, blank=True, null=True)
#     amount = models.PositiveIntegerField(default=0)
#     timestamp = models.DateTimeField(blank=True, null=True)
#     unique_id = models.CharField(max_length=20)

#     def __str__(self):
#         return str(self.amount)
   
#     def save(self, *args, **kwargs):
#         if self.timestamp is None:
#             self.timestamp = datetime.datetime.now()
#         super(Give, self).save(*args, **kwargs)
    
class Invoice(models.Model):
    description = models.TextField(max_length=300, blank=True, null=True)
    amount = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=20)
    give = models.BooleanField(default=True)

    def __str__(self):
        return str(self.amount)
    def save(self, *args, **kwargs):
        if self.timestamp is None:
            self.timestamp = datetime.datetime.now()
        super(Invoice, self).save(*args, **kwargs)
   
    
class khata(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    order_id = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("khata:detail", kwargs={"pk": self.pk})
