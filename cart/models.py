from django.db import models
from products.models import Product
from shop.models import WholeSeller, Shop 
import datetime
# class CartManager(models.Manager):
    # def get_queryset(self):
    #     return ProductQuerySet(self.model, using=self._db)

    # # def all(self):
    # #     return self.get_queryset()

    # # def featured(self):
    # #     return self.get_queryset().featured()

    # def get_by_id(self, id):
    #     qs = self.get_queryset().filter(id=id, is_active=True) # Product.objects == self.get_queryset()
    #     return qs
        

    # def search(self, query):
    #     return self.get_queryset().search(query)

    # def get_by_vendor(self, id):
    #     qs = self.get_queryset().filter(vendor=id)  # Product.objects == self.get_queryset()
    #     if qs.count() == 1:
    #         return qs.first()
    #     return None






class CartProduct(models.Model):
    vendor = models.ForeignKey(WholeSeller, on_delete=models.DO_NOTHING, null=True, blank=True)
    vendor_location = models.CharField(max_length=255, default="Null")
    product    = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    subtotal    = models.PositiveIntegerField(default=0)
    order_id   = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    # objects = CartManager()

    def __str__(self):
        return str(self.id)
    def save(self, *args, **kwargs):
        if self.timestamp is None:
            self.timestamp = datetime.datetime.now()
        super(CartProduct, self).save(*args, **kwargs)