from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=6, decimal_places=2)
    mes_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('mes_date',)

