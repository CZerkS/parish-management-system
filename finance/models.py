from django.db import models
from sacrament.models import Profile

class Invoice(models.Model):
    date_issued = models.DateField()
    or_number = models.IntegerField()
    received_by = models.CharField(max_length=255) # name that appears on the actual invoice
    profile_A = models.ForeignKey(
        Profile, 
        on_delete=models.PROTECT,
        related_name='profile_A',
        null=True, 
        blank=True
    )
    profile_B = models.ForeignKey(
        Profile, 
        on_delete=models.PROTECT,
        related_name='profile_B',
        null=True, 
        blank=True
    )
    # def __str__(self):
    #     return or_number.str()

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        'Invoice', 
        on_delete=models.CASCADE,
        related_name='invoice_items',
    )
    item_type = models.ForeignKey(
        'ItemType', 
        on_delete=models.CASCADE,
        related_name='item_type',
    )
    quantity = models.IntegerField() # defaults to 1 if item type is sacrament
    balance = models.DecimalField(max_digits=16, decimal_places=2)  # the amount needed to be paid (remaining)
    amount_paid = models.DecimalField(max_digits=16, decimal_places=2) # actual amount paid
    
    # the next invoice item's balance is computed by this invoice items's balance and amount_paid.
    # def __str__(self):
        # return item_type.__str__()

class ItemType(models.Model):
    name = models.CharField(max_length=255)
    suggested_price = models.DecimalField(max_digits=16, decimal_places=2)

    def __str__(self):
        return self.name