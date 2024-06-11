from django.db import models
from django.utils import timezone
from django.forms.fields import FloatField as FloatFormField
# Create your models here.


class StockEquitiesModel(models.Model):
    SYMBOL = models.CharField(max_length=120,default=None)
    OPEN = models.FloatField(default=0.0)
    HIGH = models.FloatField(default=0.0)
    LOW = models.FloatField(default=0.0)
    CLOSE = models.FloatField(default=0.0)
    TOTTRDQTY = models.CharField(max_length=120,default=None)
    TOTTRDVAL = models.CharField(max_length=120, default= None, blank=True, null=True, editable=False)
    TIMESTAMP = models.CharField(max_length=120,default=None)
    def __str__(self) -> str:
        return self.SYMBOL + ' | '+ str(self.TIMESTAMP)


class IndexHistoricalModel(models.Model):
    SYMBOL = models.CharField(max_length=120,default=None)
    OPEN = models.FloatField(default=0.0)
    HIGH = models.FloatField(default=0.0)
    LOW = models.FloatField(default=0.0)
    CLOSE = models.FloatField(default=0.0)
    TOTTRDQTY = models.CharField(max_length=120,default=None)
    TOTTRDVAL = models.CharField(max_length=120, default= None, blank=True, null=True, editable=False)
    TIMESTAMP = models.DateField(default=None)

    def __str__(self) -> str:
        return self.SYMBOL + ' | '+ str(self.TIMESTAMP)
    