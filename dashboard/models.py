from django.db import models
from django.contrib.auth.models import User
from shop.models import Shop
from manufacturer.models import Manufacturer
from service.models import Service


class Seller(models.Model):
    user = models.OneToOneField(User)

    def is_seller(self, id):
        if Shop.objects.is_exist(id):
            return True
        elif Manufacturer.objects.is_exist(id):
            return True