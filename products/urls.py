from django.urls import path
from .views import ProductListCreate, ProductDetails

urlpatterns = [
    path("", ProductListCreate.as_view(), name="product-list-create"),
    path("<int:id>/", ProductDetails.as_view(), name="product-detail"),
]
