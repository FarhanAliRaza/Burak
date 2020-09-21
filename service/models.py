from django.db import models
import os
import random
from ecom import settings
User = settings.AUTH_USER_MODEL

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):

    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "service/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )


class ServiceSubCategory(models.Model):
    service_sub_category = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.service_sub_category


main_category = (
    ('Shop', 'Shop'),
    ('Manufacturer', 'Manufacturer'),
    ('Service', 'Service')
)


class ServiceManager(models.Manager):

    def is_exist(self, k):
        qs = self.filter(vendor=k)  # Product.objects == self.get_queryset()
        if qs:
            return True
        else:
            return False


class Service(models.Model):
    vendor = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    name = models.CharField(max_length=255)
    main_category = models.CharField(max_length=2, choices=main_category, default='sh')
    sub_category = models.ForeignKey(ServiceSubCategory, on_delete=models.DO_NOTHING)
    free_pickup_and_delivery = models.BooleanField(default=False)

    objects = ServiceManager()

