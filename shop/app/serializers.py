from rest_framework import serializers
from .models import Category, Product, Review


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    added_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    category_id = serializers.IntegerField()
    description = serializers.CharField()
    added_at = serializers.DateTimeField(read_only=True)
    quantity = serializers.IntegerField(default=0)
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.description = validated_data.get('description', instance.description)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
    
    
class ReviewSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Review.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance