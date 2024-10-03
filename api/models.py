from django.db import models

# Create your models here
class Certificate(models.Model):
    domain = models.CharField(max_length=255)
    certificate_type = models.CharField(max_length=100)
    subscription_period = models.CharField(max_length=100)
    certificate_issued = models.DateField()

    def __str__(self):
        return self.domain


class Domain(models.Model):
    domain_name = models.CharField(max_length=255)
    auto_renew = models.CharField(max_length=10)
    lock = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    expiration_date = models.DateField()
    privacy = models.CharField(max_length=10)
    nameservers = models.TextField()
    estimated_value = models.CharField(max_length=50)
    create_date = models.DateField()
    renewal_price = models.CharField(max_length=50)
    protection_plan = models.CharField(max_length=50)
    ownership_date = models.DateField()

    def __str__(self):
        return self.domain_name
