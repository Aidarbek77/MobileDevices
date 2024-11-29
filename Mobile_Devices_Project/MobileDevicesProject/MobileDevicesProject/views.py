from .models import Device, Category
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import DeviceForm

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'devices/device_list.html', {'devices': devices})

def device_list_by_category(request):
    category_id = request.GET.get('category')  # ID категории из Query Parameters
    devices = Device.objects.filter(category_id=category_id) if category_id else Device.objects.all()
    categories = Category.objects.all()  # Для отображения всех категорий
    return render(request, 'devices/device_list_by_category.html', {'devices': devices, 'categories': categories})

def device_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)  # Устройство по ID
    return render(request, 'devices/device_detail.html', {'device': device})

def home(request):
    devices = Device.objects.all()  # Получаем все устройства
    return render(request, 'devices/home.html', {'devices': devices})

def add_device(request):
    if request.method == "POST":
        form = DeviceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeviceForm()
    return render(request, 'devices/add_device.html', {'form': form})

def edit_device(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == "POST":
        form = DeviceForm(request.POST, request.FILES, instance=device)
        if form.is_valid():
            form.save()
            return redirect('device_detail', device_id=device.id)
    else:
        form = DeviceForm(instance=device)
    return render(request, 'devices/edit_device.html', {'form': form, 'device': device})

from django.shortcuts import get_object_or_404

def delete_device(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == "POST":
        device.delete()
        return redirect('home')
    return render(request, 'devices/delete_device.html', {'device': device})
