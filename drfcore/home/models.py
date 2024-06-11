from django.db import models
from django.utils import timezone
from django.forms.fields import FloatField as FloatFormField
class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class NotesModel(models.Model):
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 4000)
    tags = models.CharField(max_length = 600)
    reactions = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    updated = AutoDateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title


class StockFuturesModel(models.Model):
    SYMBOL = models.CharField(max_length=120,default=None)
    OPEN = models.FloatField(default=0.0)
    HIGH = models.FloatField(default=0.0)
    LOW = models.FloatField(default=0.0)
    CLOSE = models.FloatField(default=0.0)
    VOLUME = models.FloatField(default=0.0)
    OPEN_INT = models.FloatField(max_length=120,default=None)
    CHG_IN_OI = models.FloatField(default=0.0)
    TIMESTAMP = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.SYMBOL + ' | '+ str(self.TIMESTAMP)