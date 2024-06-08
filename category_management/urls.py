from django.urls import path
from .views import *

urlpatterns = [
    path("", CategoryListCreate.as_view(), name="category-list-create"),
    path("<uuid:id>/", CategoryDetails.as_view(), name="category-detail"),
]
