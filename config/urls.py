from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("category/", include("category_management.urls")),
    path("warehouse/", include("warehouse_management.urls")),
]
