from django.db import models

# Create your models here.

class BapiConfig(models.Model):
    bank_name = models.CharField(max_length=100, unique=True)
    bank_service_id = models.IntegerField(max_length=100, default=123)
    bank_pubkey_id = models.CharField(max_length=100, default='123')