from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.RestaurantListCreateAPIView.as_view()),
    path('restaurants/<int:pk>/', views.RestaurantRetrieveUpdateDestroyAPIView.as_view()),
    path('restaurants/<str:slug>/', views.RestaurantRetrieveUpdateDestroyAPIView.as_view(lookup_field='slug')),


    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('categories/<str:slug>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(lookup_field='slug')),

    path('products/', views.ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('products/<str:slug>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(lookup_field='slug')),

    path('upload/', views.upload_image),
]