from django.db import models


class Device(models.Model):
    CPU_model = models.CharField(max_length=1024)
    Memory_info = models.CharField(max_length=1024)
    System_info = models.CharField(max_length=1024)
    def __str__(self):
        return self.CPU_model
