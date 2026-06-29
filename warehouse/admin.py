from django.contrib import admin
from .models import SKU, StorageBin, Order

@admin.register(SKU)
class SKUAdmin(admin.ModelAdmin): # Убрали лишнее .admin
    list_display = ('name', 'barcode', 'weight')

@admin.register(StorageBin)
class BinAdmin(admin.ModelAdmin): # Убрали лишнее .admin
    list_display = ('bin_code', 'is_occupied')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): # Убрали лишнее .admin
    list_display = ('id', 'sku', 'status')