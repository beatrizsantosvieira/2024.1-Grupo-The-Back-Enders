from django.db import models

class Camera(models.Model):
    company = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    specific_location = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    network_stream_protocol = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    port = models.IntegerField()
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.specific_location
    class Meta:
        app_label = 'cameras'
