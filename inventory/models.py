from django.db import models


class Art(models.Model):
    art_id = models.IntegerField(primary_key=True)
    art = models.ImageField(upload_to='inventory/art/%Y/%m/%d')
    title = models.CharField(max_length=100, blank=False, null=False)
    artist = models.CharField(max_length=50, blank=False, null=False)
    quantity = models.PositiveIntegerField(blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False)

    class Meta:
        ordering = ['-art_id']

    def __str__(self):
        return f'Art ID:{self.art_id} {self.art} [{self.title}] -{self.artist} [남은 수량:{self.quantity}] ￦{self.price}'

    def get_absolute_url(self):
        return f'/sale/{self.pk}/'
