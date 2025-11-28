from django.db import models


# Create your models here.
#TODO 例題８ Buyerテーブル
class Buyer(models.Model):
    buy_code = models.IntegerField(primary_key=True)
    buy_name = models.CharField(max_length=12, blank=True, null=True)
    staff_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buyer' #テーブル名の指定
