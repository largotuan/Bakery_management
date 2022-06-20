from django.db import models
from Bakery_Management.models import TrackingAbstractModel, NameAbstractModel
# Create your models here.


class Category(TrackingAbstractModel, NameAbstractModel):

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'

    def save_name(self):
        self.name = self.name.upper()
        self.save()


class Transaction(TrackingAbstractModel, NameAbstractModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    note = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f'{self.name} - {self.category} - {self.amount} - {self.note}'


