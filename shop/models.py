from django.db import models
from ecom import settings
User = settings.AUTH_USER_MODEL
import os
import random
from django.urls import reverse
from django.shortcuts import get_object_or_404

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):

    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "shop/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )



# main_category = (
#     ('Shop', 'Shop'),
#     ('Manufacturer', 'Manufacturer'),
#     ('Service', 'Service')
# )


class ShopManager(models.Manager):

    def is_exist(self, k):
        qs = self.filter(vendor=k)  # Product.objects == self.get_queryset()
        if qs:
            return True
        else:
            return False
    def get_by_id(self, pk):
        qs = Shop.objects.filter(pk=pk)
        return qs


class Shop(models.Model):

    vendor = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    # main_category = models.CharField(max_length=20, choices=main_category, default='sh')
    # sub_category = models.ForeignKey(ShopSubCategory, on_delete=models.DO_NOTHING)

    objects = ShopManager()

    def __str__(self):
        return self.name


class WholeSellerManager(models.Manager):

    def is_exist(self, k):
        qs = self.filter(vendor=k)  # Product.objects == self.get_queryset()
        if qs:
            return True
        else:
            return False
    def get_by_id(self, pk):
        qs = Shop.objects.filter(pk=pk)
        return qs
       

class WholeSeller(models.Model):

    vendor = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    # main_category = models.CharField(max_length=20, choices=main_category, default='sh')
    # sub_category = models.ForeignKey(ShopSubCategory, on_delete=models.DO_NOTHING)

    objects = WholeSellerManager()

    def __str__(self):
        return self.location
    def save(self, *args, **kwargs):
        self.vendor.is_vendor = True
        self.vendor.save()
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("shop:shops", kwargs={"pk": self.pk})
