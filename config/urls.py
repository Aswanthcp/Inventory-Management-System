from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("category/", include("category.urls")),
    path("warehouse/", include("warehouse.urls")),
    path("supplier/", include("supplier.urls")),
    path("product/", include("products.urls")),
]
