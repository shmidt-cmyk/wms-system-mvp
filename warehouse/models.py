from django.db import models

class SKU(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование товара")
    barcode = models.CharField(max_length=50, unique=True, verbose_name="Штрих-код")
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Вес")
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sku'

class StorageBin(models.Model):
    bin_code = models.CharField(max_length=20, unique=True, verbose_name="Код ячейки")
    is_occupied = models.BooleanField(default=False, verbose_name="Занята")

    def __str__(self):
        return self.bin_code

    class Meta:
        db_table = 'storage_bin'

class Order(models.Model):
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    bin = models.ForeignKey(StorageBin, on_delete=models.SET_NULL, null=True)
    status = models.CharField(
        max_length=20, 
        default='new',
        choices=[
            ('new', 'Новый'),
            ('picking', 'Сборка'),
            ('packed', 'Упакован'),
            ('shipped', 'Отгружен'),
            ('cancelled', 'Отказ/Отмена'),
        ]
    )

    def __str__(self):
        return f"Заказ #{self.id} - {self.sku.name}"

    class Meta:
        db_table = 'orders'