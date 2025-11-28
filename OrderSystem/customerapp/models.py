from django.db import models


# Create your models here.
class Customer(models.Model):
    cust_code = models.IntegerField(primary_key=True)
    cust_name = models.CharField(max_length=12, blank=True, null=True)
    staff_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'
