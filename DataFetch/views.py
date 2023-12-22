from django.shortcuts import render
from .models import *
from datetime import datetime


def GetAllInfos(request):
    if request.method == "GET":
        context = {}
        device = Device.objects.all().order_by('-created_at').first()
        context['device'] = device
        return render(request, "tables.html", context)
    
# def PostInfos(request):
#     if request.method == "POST":
#         context = {}
#         data = request.POST
#         device = Device.objects.create(CPU_model=data['cpu_model'],Memory_info=data['memory_information'],System_info=data['system_information'])
#         device.save()
#         return render(request)

import json
from django.http import JsonResponse
from .models import Device
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def PostInfos(request):
    if request.method == "POST":
        try:
            json_data = json.loads(request.body)
            cpu_model = json_data.get('cpu_model', '')
            memory_info = json_data.get('memory_information', '')
            system_info = json_data.get('system_information', '')
            ip_address = json_data.get('ip_address', '')
            username = json_data.get('username', '')

            device = Device.objects.create(IP_Address=ip_address, UserName=username,CPU_model=cpu_model, Memory_info=memory_info, System_info=system_info, created_at=datetime.now())
            device.save()

            # Return a JSON response indicating success
            return JsonResponse({'message': 'Device information saved successfully.'}, status=201)
        except json.JSONDecodeError:
            # Handle invalid JSON data
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
    else:
        # Handle other HTTP methods (GET, PUT, DELETE, etc.)
        return JsonResponse({'error': 'Invalid request method.'}, status=405)

