from rest_framework import generics
from .serializers import CategorySerializers
from .models import CategoryModels
from rest_framework.permissions import IsAuthenticated, AllowAny

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = CategoryModels.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]
    
  

class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModels.objects.all()
    serializer_class = CategorySerializers
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
