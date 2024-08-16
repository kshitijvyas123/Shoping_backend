from rest_framework import serializers
from .models import Products


class ProductsSerilizar(serializers.ModelSerializer):
   class Meta:
      model = Products
      fields = ["name", "description", "image", "price","qty","reviews","availability","brand",
                "category","sku","size","previousPrice","color"]


