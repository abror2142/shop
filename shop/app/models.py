from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name
    
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.content