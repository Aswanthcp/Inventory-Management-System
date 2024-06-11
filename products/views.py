from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, ProductCreateSerializer
from rest_framework.permissions import IsAuthenticated


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return ProductSerializer

    def create(self, request, *args, **kwargs):
        create_serializer = self.get_serializer(data=request.data)
        create_serializer.is_valid(raise_exception=True)

        product = Product.objects.create(**create_serializer.validated_data)

        display_serializer = ProductSerializer(product)

        return Response(display_serializer.data, status=status.HTTP_201_CREATED)


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        warehouse_id = request.data.get("warehouse")
        if warehouse_id:
            instance.warehouse_id = warehouse_id

        self.perform_update(serializer)
        updated_instance = self.get_object()
        display_serializer = ProductSerializer(updated_instance)
        return Response(display_serializer.data)
