from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, primary_key=True, on_delete=models.CASCADE, related_name='measurement',
                               unique=False)
    temperature = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
