from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()

    def __str__(self):
        return self.name
