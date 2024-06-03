from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'app_camera_system'

class CameraPark(models.Model):
    company = models.ForeignKey(Company, related_name='camera_parks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'app_camera_system'

class Camera(models.Model):
    camera_park = models.ForeignKey(CameraPark, related_name='cameras', on_delete=models.CASCADE)
    specific_location = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    network_stream_protocol = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    port = models.IntegerField()
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.company.name}"

    class Meta:
        app_label = 'app_camera_system'
