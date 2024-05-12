from django.db import models

class Camera(models.Model):
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    is_enabled = models.BooleanField(default=True)
    specific_location = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    compression_format = models.CharField(max_length=100)
    network_stream_protocol = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    port = models.IntegerField()
    company = models.CharField(max_length=100)

    class Meta:
        app_label = 'cameras'
