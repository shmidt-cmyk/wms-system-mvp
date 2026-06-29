from django.shortcuts import render
from .models import SKU, StorageBin, Order
from django.db.models import Count

def dashboard(request):
    # 1. Общие KPI
    total_sku = SKU.objects.count()
    total_orders = Order.objects.count()
    
    # 2. Складские мощности
    total_bins = StorageBin.objects.count()
    occupied_bins = StorageBin.objects.filter(is_occupied=True).count()
    free_bins = total_bins - occupied_bins
    
    # 3. Данные для графиков (ВАЖНЫЙ БЛОК!)
    status_data = Order.objects.values('status').annotate(count=Count('id'))
    
    # Создаем списки, которые "потерялись" на скриншоте
    labels = [item['status'].capitalize() for item in status_data]
    counts = [item['count'] for item in status_data]

    context = {
        'total_sku': total_sku,
        'total_orders': total_orders,
        'occupied_bins': occupied_bins,
        'free_bins': free_bins,
        'total_bins': total_bins,
        'status_labels': labels,
        'status_counts': counts,
    }
    return render(request, 'dashboard.html', context)

def mobile_scan(request):
    # Логика: получаем список новых заказов для работы кладовщика
    orders = Order.objects.filter(status='new')
    return render(request, 'mobile_scan.html', {'orders': orders})