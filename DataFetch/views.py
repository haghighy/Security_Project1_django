from django.shortcuts import render
from .models import *


def GetAllInfos(request):
    if request.method == "GET":
        context = {}
        device = Device.objects.all()
        context['device'] = device
        return render(request, "tables.html", context)
    
def PostInfos(request):
    if request.method == "POST":
        context = {}
        data = request.POST
        device = Device.objects.create(CPU_model=data['cpu_model'],Memory_info=data['memory_information'],System_info=data['system_information'])
        device.save()
        return render(request, "tables.html")
