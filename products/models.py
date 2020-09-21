import random
import os
from django.db import models
from django.db.models import Q, PositiveIntegerField
from django.urls import reverse
from ecom import settings
User = settings.AUTH_USER_MODEL
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from shop.models import WholeSeller


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

siza_160 = (160, 160)
size_33 = ()
def upload_image_path(instance, filename):

    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )


class ProductQuerySet(models.query.QuerySet):

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (
                  Q(title__icontains=query) |
                  Q(amount__icontains=query) |
                  Q(price__icontains=query)
                  #Q(tag__title__icontains=query)
                  )
        return self.filter(lookups).distinct()


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().search(query)

    def get_by_vendor(self, id):
        qs = self.get_queryset().filter(vendor=id)  # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

class Category(models.Model):
    category = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    thumbnail = ImageSpecField(
        source = 'image',
        processors=[ResizeToFill(800, 400)],
        format='jpeg',
        options={'quality': 70}
    )
    def __str__(self):
        return self.category
    def get_absolute_url(self):
        return reverse("products:list", kwargs={"slug": self.slug})

class Product(models.Model):
    vendor = models.ForeignKey(WholeSeller, on_delete=models.DO_NOTHING)
    vendor_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    amount = models.CharField(null=True, blank=True, max_length=255)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    thumbnail = ImageSpecField(
        source = 'image',
        processors=[ResizeToFill(160, 160)],
        format='jpeg',
        options={'quality': 70}
    )
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.DO_NOTHING)
    # sub_category = models.CharField(max_length=255)
    # description = models.TextField(max_length=1000)
    # icst = models.CharField(default="90 Minutes", max_length=20)
    # ocst = models.CharField(choices=time_choices, default="1 day", max_length=10)
    # pickup_delivery_free = models.BooleanField(default=False)
    objects = ProductManager()

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk": self.pk})
    def __str__(self):
        return self.title

    @property
    def name(self):
        return self.title
