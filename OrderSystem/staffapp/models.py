from django.db import models


class Staff(models.Model):
    staff_code = models.IntegerField(primary_key=True)
    staff_name = models.CharField(max_length=12, blank=True, null=True)
    work_years = models.IntegerField(blank=True, null=True)
    wages = models.IntegerField(blank=True, null=True)
    staff_img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'
#        verbose_name = 'スタッフ'
