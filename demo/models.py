from django.db import models


class OrderModels(models.Model):
    seller_id = models.IntegerField(null=False, default=0)
    tracking_number = models.CharField(null=False, max_length=100)
    country = models.CharField(max_length=100)
    updated_time = models.IntegerField(default=0)
    create_time = models.IntegerField(default=0)

    def __str__(self):
        return self.tracking_number
