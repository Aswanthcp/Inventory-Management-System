from django.urls import path
from .views import *

urlpatterns = [
    path("", WarehouseListCreate.as_view(), name="warehouse-list-create"),
    path("<uuid:id>/", WarehouseDetails.as_view(), name="warehouse-detail"),
]
