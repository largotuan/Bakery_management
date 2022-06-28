from django.db import models
from django.forms import ModelForm
from Bakery_Management.models import TrackingAbstractModel, NameAbstractModel
from product_management.constants import QuantityType
from django.core.exceptions import ValidationError
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
    action = models.IntegerField(default=QuantityType.ADD, choices=QuantityType.ACTION_CHOICES)
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
    def add_action(self):
        quantity_dict = dict(QuantityType.ACTION_CHOICES)
        return quantity_dict.get(self.action)

    # def action(self):
    #     action = str(QuantityType.ACTION_CHOICES)
    #     return self.action

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.price = self.product.price
        super(History, self).save(force_insert, force_update, using, update_fields)
        if self.action == QuantityType.ADD:
            self.product.quantity += self.quantity
        elif self.action == QuantityType.EXPIRED:
            if self.product.quantity < self.quantity:
                raise ValueError(
                    "Cannot update history because current_quantity < expired_quantity."
                )
            else:
                self.product.quantity -= self.quantity
        else:
            if self.product.quantity < self.quantity:
                raise ValidationError("Cannot update history because product_quantity < quantity.")
            self.product.quantity = self.quantity
        self.product.save()
