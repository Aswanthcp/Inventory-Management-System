from rest_framework import serializers
from .models import CategoryModels


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModels
        fields = "__all__"
