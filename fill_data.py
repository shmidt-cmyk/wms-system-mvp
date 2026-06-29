import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logistics_core.settings')
django.setup()

from warehouse.models import SKU, StorageBin, Order

def run():
    # 1. Товары (используем update_or_create)
    items = [
        ("Автоматический выключатель", "4601234567001", 0.25),
        ("Кабель-канал 25х16", "4601234567002", 12.0),
        ("Светодиодный прожектор", "4601234567003", 1.1),
        ("Счетчик электроэнергии", "4601234567004", 0.8),
        ("Шкаф телекоммуникационный", "4601234567005", 28.5),
        ("Стабилизатор напряжения", "4601234567006", 14.2),
        ("Изолятор фарфоровый", "4601234567007", 3.5),
        ("Муфта кабельная", "4601234567008", 2.1),
        ("Коробка распределительная", "4601234567009", 0.15),
        ("Шина медная", "4601234567010", 1.42),
        ("Контактор", "4601234567011", 0.95),
        ("Реле контроля фаз", "4601234567012", 0.3),
        ("Подрозетник", "4601234567013", 0.05),
        ("Гофра ПВХ", "4601234567014", 2.4),
        ("Клеммник", "4601234567015", 0.45),
    ]

    print("Загружаю товары...")
    for name, code, w in items:
        SKU.objects.update_or_create(
            barcode=code,
            defaults={'name': name, 'weight': w}
        )

    # 2. Ячейки (теперь безопасно)
    print("Размечаю ячейки...")
    for i in range(1, 25):
        StorageBin.objects.update_or_create(
            bin_code=f"D-{i:02d}-01",
            defaults={'is_occupied': random.choice([True, False])}
        )

    # 3. Заказы (удаляем старые и создаем 40 новых для красоты графиков)
    print("Генерирую оперативную сводку...")
    Order.objects.all().delete() 
    
    skus = list(SKU.objects.all())
    bins = list(StorageBin.objects.all())
    statuses = ['new', 'picking', 'packed', 'shipped', 'cancelled']

    for _ in range(40):
        Order.objects.create(
            sku=random.choice(skus),
            bin=random.choice(bins),
            status=random.choice(statuses)
        )
    print("--- МИССИЯ ВЫПОЛНЕНА: ДАННЫЕ СИНХРОНИЗИРОВАНЫ ---")

if __name__ == '__main__':
    run()