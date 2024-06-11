from django.urls import path
from .views import *

urlpatterns = [
    path("", SuppliersListCreate.as_view(), name="warehouse-list-create"),
    path("<uuid:id>/", SuppliersDetails.as_view(), name="warehouse-detail"),
    path("<uuid:id>/products/", SupplierProductsList.as_view(), name='supplier-products'),
]
