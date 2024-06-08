from django.db import models
from category.models import CategoryModels
from warehouse.models import WarehouseModels
from supplier.models import SupplierModels  # Assume there's a supplier app


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryModels, on_delete=models.CASCADE)
    supplier = models.ForeignKey(SupplierModels, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(WarehouseModels, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    low_stock_threshold = models.IntegerField(default=10)

    def __str__(self):
        return self.name
