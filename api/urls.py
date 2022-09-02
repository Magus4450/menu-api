from django.urls import path

from . import routers, views

urlpatterns = [

    path('restaurants/', routers.restaurantListCreateRouter),
    # path('restaurants/', views.restaurantRouter),

    # path('restaurants/<int:pk>/', views.RestaurantUpdateAPIView.as_view()),
    # path('restaurants/<int:pk>/', views.RestaurantDestroyAPIView.as_view()),
    # path('restaurants/<int:pk>/', views.RestaurantRetrieveAPIView.as_view()),

    # path('restaurants/<str:slug>/', views.RestaurantUpdateAPIView.as_view(lookup_field='slug')),
    # path('restaurants/<str:slug>/', views.RestaurantDestroyAPIView.as_view(lookup_field='slug')),
    # path('restaurants/<str:slug>/', views.RestaurantRetrieveAPIView.as_view(lookup_field='slug')),


    path('restaurants/<int:pk>/', routers.restaurantRetrieveUpdateDestroyRouter),
    path('restaurants/<str:slug>/', routers.restaurantRetrieveUpdateDestroyRouter),



    # path('categories/', views.CategoryCreateAPIView.as_view()),
    # path('categories/', views.CategoryListAPIView.as_view()),

    path('categories/', routers.categoryListCreateRouter),
    path('categories/<int:pk>/', routers.categoryRetrieveUpdateDestroyRouter),
    path('categories/<str:slug>/', routers.categoryRetrieveUpdateDestroyRouter),

    # path('categories/<int:pk>/', views.CategoryRetrieveAPIView.as_view()),
    # path('categories/<int:pk>/', views.CategoryDestroyAPIView.as_view()),
    # path('categories/<int:pk>/', views.CategoryUpdateAPIView.as_view()),

    # path('categories/<str:slug>/', views.CategoryDestroyAPIView.as_view(lookup_field='slug')),
    # path('categories/<str:slug>/', views.CategoryUpdateAPIView.as_view(lookup_field='slug')),

    # path('products/', views.ProductListAPIView.as_view()),
    # path('products/', views.ProductCreateAPIView.as_view()),

    # path('products/<int:pk>/', views.ProductUpdateAPIView.as_view()),
    # path('products/<int:pk>/', views.ProductDestroyAPIView.as_view()),
    # path('products/<int:pk>/', views.ProductRetrieveAPIView.as_view()),

    # path('products/<str:slug>/', views.ProductUpdateAPIView.as_view(lookup_field='slug')),
    # path('products/<str:slug>/', views.ProductDestroyAPIView.as_view(lookup_field='slug')),
    # path('products/<str:slug>/', views.ProductRetrieveAPIView.as_view(lookup_field='slug')),

    path('products/', routers.productListCreateRouter),
    path('products/<int:pk>/', routers.productRetrieveUpdateDestroyRouter),
    path('products/<str:slug>/', routers.productRetrieveUpdateDestroyRouter),

    path('upload/', views.upload_image),
]
