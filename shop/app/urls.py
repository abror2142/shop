from django.urls import path
from .views import (CategoryListCreateAPI, CategoryRetrieveUpdateDestroyAPI, 
                    ProductListCreateAPI, ProductRetrieveUpdateDestroyAPI,
                    ReviewListCreateAPI, ReviewRetrieveUpdateDestroyAPI)


urlpatterns = [
    path('category/list/', CategoryListCreateAPI.as_view()),
    path('category/detail/<int:pk>/', CategoryRetrieveUpdateDestroyAPI.as_view()),
    path('product/list/', ProductListCreateAPI.as_view()),
    path('product/detail/<int:pk>/', ProductRetrieveUpdateDestroyAPI.as_view()),
    path('review/list/', ReviewListCreateAPI.as_view()),
    path('review/detail/<int:pk>/', ReviewRetrieveUpdateDestroyAPI.as_view()),
]
