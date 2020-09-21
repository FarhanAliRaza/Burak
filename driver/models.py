from django.db import models
from ecom.settings import AUTH_USER_MODEL
User = AUTH_USER_MODEL
class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="known")
    location = models.TextField(default="known")
    vehicle = models.CharField(max_length=255, default="known")
    for_shops = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    