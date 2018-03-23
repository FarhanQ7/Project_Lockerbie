from django.db import models

# Create your models here.

class Price(models.Model):

    stockPrice = models.CharField(max_length=264)
    Time =  models.TimeField()

    def __str__(self):
        return self.stcokPrice


class Symbol_record(models.Model):
    sPrices = models.ForeignKey(Price)
    Name = models.CharField(max_length=264,unique=True)



