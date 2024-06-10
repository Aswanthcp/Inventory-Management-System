from rest_framework import generics
from .serializers import CategorySerializers
from .models import CategoryModels


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = CategoryModels.objects.all()
    serializer_class = CategorySerializers
    
  

class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModels.objects.all()
    serializer_class = CategorySerializers
    lookup_field = "id"
