from django.db import models
from shop.models import WholeSeller, Shop
from products.models import Product
from cart.models import CartProduct
from django.utils import timezone
from ecom.settings import AUTH_USER_MODEL
User = AUTH_USER_MODEL
import datetime
from django.shortcuts import reverse
# class OrderManager(models.Manager):
    # def get_queryset(self):
    #     return ProductQuerySet(self.model, using=self._db)

    # def all(self):
    #     return self.get_queryset()

    # def featured(self):
    #     return self.get_queryset().featured()

    # def get_by_id(self, id):
    #     qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
    #     if qs.count() == 1:
    #         return qs.first()
    #     return None

    # def search(self, query):
    #     return self.get_queryset().search(query)

    # def get_by_vendor(self, id):
    #     qs = self.get_queryset().filter(vendor=id)  # Product.objects == self.get_queryset()
    #     if qs.count() == 1:
    #         return qs.first()
    #     return None



class Order(models.Model):
    ordered_by = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)
    delivery_loaction = models.CharField(max_length=255, blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    order_id = models.CharField(max_length=20, null=True, blank=True)
    cart = models.ManyToManyField(CartProduct)
    total = models.PositiveIntegerField()
    timestamp = models.DateTimeField()
   
    def __str__(self):
        return str(self.pk)

   
    def save(self, *args, **kwargs):
        if self.timestamp is None:
            self.timestamp = datetime.datetime.now()
        super(Order, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("order:detail", kwargs={"pk": self.pk})

class ShopOrder(models.Model):
    wholeseller = models.ForeignKey(WholeSeller, on_delete=models.DO_NOTHING)
    is_complete = models.BooleanField(default=False)
    order_id = models.CharField(max_length=20, null=True, blank=True)
    cart = models.ManyToManyField(CartProduct)
    total = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
   
    def __str__(self):
        return str(self.pk)

   
    def save(self, *args, **kwargs):
        if self.timestamp is None:
            self.timestamp = datetime.datetime.now()
        super(ShopOrder, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("order:detail", kwargs={"pk": self.pk})

