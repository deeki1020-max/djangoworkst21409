from django.db import models


class Goods(models.Model):
    goods_code = models.CharField(primary_key=True, max_length=4)
    goods_name = models.CharField(max_length=40, blank=True, null=True)
    classify = models.CharField(max_length=12, blank=True, null=True)
    sl_price = models.IntegerField(blank=True, null=True)
    cs_price = models.IntegerField(blank=True, null=True)
    stocks = models.SmallIntegerField(blank=True, null=True)
    buy_code = models.IntegerField(blank=True, null=True)
    goods_img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods'
