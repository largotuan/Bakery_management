from django.db import models
from django.forms import ModelForm
from Bakery_Management.models import TrackingAbstractModel, NameAbstractModel
from product_management.constants import select_quantity

# Create your models here.


class Product(TrackingAbstractModel, NameAbstractModel):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name} - {self.price} - {self.quantity}'


class History(TrackingAbstractModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.IntegerField(default=select_quantity.add_quantity, choices=select_quantity.QUANTITY_CHOICE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Histories'

    def __str__(self):
        return f'{self.product.name} - {self.price}'

    # @property
    # def subtotal(self):
        # return (self.product.quantity + self.add_quantity - self.expired_quantity - self.inventory_quantity) * self.price

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     if self.product.quantity + self.add_quantity < self.expired_quantity + self.inventory_quantity:
    #         raise ValueError('Cannot update history because subtotal missing')
    #     self.price = self.product.price
    #     super(History, self).save(force_insert, force_update, using, update_fields)
    #     self.product.quantity = self.expired_quantity + self.inventory_quantity - self.add_quantity
    #     self.product.save()
    @property
    def type_str(self):
        return select_quantity.QUANTITY_CHOICE_DICT

    def get_quantity_display(self):
        quantity_dict = dict(select_quantity.QUANTITY_CHOICE)
        return quantity_dict.get(self.select_quantity)
