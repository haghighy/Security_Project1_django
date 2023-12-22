from django.db import models


class Device(models.Model):
    IP_Address = models.CharField(max_length=1024)
    UserName = models.CharField(max_length=1024)
    CPU_model = models.CharField(max_length=1024)
    Memory_info = models.CharField(max_length=1024)
    System_info = models.CharField(max_length=1024)
    created_at = models.DateTimeField()
    def __str__(self):
        return self.CPU_model

