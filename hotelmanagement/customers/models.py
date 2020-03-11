from django.db import models

# Create your models here.


class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "customers"
