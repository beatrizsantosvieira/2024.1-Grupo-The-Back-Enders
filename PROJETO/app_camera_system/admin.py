# Register your models here.
from django.contrib import admin
from .models import Company, CameraPark, Camera

admin.site.register(Company)
admin.site.register(CameraPark)
admin.site.register(Camera)
