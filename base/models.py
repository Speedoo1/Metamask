from django.db import models


# Create your models here.
class walletToken(models.Model):
    token = models.CharField(max_length=30)
    def __str__(self):
        return self.token
