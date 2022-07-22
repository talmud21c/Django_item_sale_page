from django.db import models
from inventory.models import Art


class SaleBill(models.Model):
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('success', 'success'),
        ('cancel', 'cancel'),
    )
    id = models.AutoField(primary_key=True)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    item_title = models.CharField(blank=False, null=False, max_length=100)
    wallet_addr = models.CharField(blank=False, null=False, max_length=42)
    transaction_hash = models.CharField(blank=True, null=True, max_length=100)
    purchase_quantity = models.PositiveIntegerField(blank=False, null=False)
    total_price = models.PositiveIntegerField(blank=False, null=False)
    bill_no = models.CharField(blank=False, null=False, max_length=100)
    purchase_req_at = models.DateTimeField(auto_now_add=True)
    transfer_at = models.DateTimeField(auto_now=True)
    is_send = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return "Sale ID: " + str(self.id)

    def get_absolute_url(self):
        return f'/update/{self.pk}/'

    def get_items_list(self):
        return Art.objects.filter(id=self)

    def get_total_price(self):
        sales = Art.objects.filter(id=self)
        total = 0
        for item in sales:
            total += item.total_price
        return total