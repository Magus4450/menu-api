from django.views.decorators.csrf import csrf_exempt

from . import views


@csrf_exempt
def restaurantListCreateRouter(request):
    if request.method == 'GET':
        return views.RestaurantListAPIView().as_view()(request)
    elif request.method == 'POST':
        return views.RestaurantCreateAPIView().as_view()(request)

@csrf_exempt
def restaurantRetrieveUpdateDestroyRouter(request, pk=None, slug=None):
    if pk:
        if request.method == 'GET':
            return views.RestaurantRetrieveAPIView().as_view()(request, pk=pk)
        elif request.method == 'PATCH' or request.method == "PUT":
            return views.RestaurantUpdateAPIView().as_view()(request, pk=pk)
        elif request.method == 'DELETE':
            return views.RestaurantDestroyAPIView().as_view()(request, pk=pk)

    elif slug:

        if request.method == 'GET':
            return views.RestaurantRetrieveAPIView().as_view(lookup_field='slug')(request, slug=slug)
        elif request.method == 'PATCH' or request.method == "PUT":
            return views.RestaurantUpdateAPIView().as_view(lookup_field='slug')(request, slug=slug)
        elif request.method == 'DELETE':
            return views.RestaurantDestroyAPIView().as_view(lookup_field='slug')(request, slug=slug)

@csrf_exempt
def categoryListCreateRouter(request):
    if request.method == 'GET':
        return views.CategoryListAPIView().as_view()(request)
    elif request.method == 'POST':
        return views.CategoryCreateAPIView().as_view()(request)
    
@csrf_exempt
def categoryRetrieveUpdateDestroyRouter(request, pk=None, slug=None):
    if pk:
        if request.method == 'GET':
            return views.CategoryRetrieveAPIView().as_view()(request, pk=pk)
        elif request.method == 'PATCH' or request.method == "PUT":
            return views.CategoryUpdateAPIView().as_view()(request, pk=pk)
        elif request.method == 'DELETE':
            return views.CategoryDestroyAPIView().as_view()(request, pk=pk)

    elif slug:

        if request.method == 'GET':
            return views.CategoryRetrieveAPIView().as_view(lookup_field='slug')(request, slug=slug)
        elif request.method == 'PATCH' or request.method == "PUT":
            return views.CategoryUpdateAPIView().as_view(lookup_field='slug')(request, slug=slug)
        elif request.method == 'DELETE':
            return views.CategoryDestroyAPIView().as_view(lookup_field='slug')(request, slug=slug)
        
@csrf_exempt
def productListCreateRouter(request):
    if request.method == 'GET':
        return views.ProductListAPIView().as_view()(request)
    elif request.method == 'POST':
        return views.ProductCreateAPIView().as_view()(request)


@csrf_exempt
def productRetrieveUpdateDestroyRouter(request, pk=None, slug=None):
    if pk:
        if request.method == 'GET':
            return views.ProductRetrieveAPIView().as_view()(request, pk=pk)
        elif request.method == 'PATCH' or request.method == "PUT":
            return views.ProductUpdateAPIView().as_view()(request, pk=pk)
        elif request.method == 'DELETE':
            return views.ProductDestroyAPIView().as_view()(request, pk=pk)
    elif slug:
        if request.method == 'GET':
            return views.ProductRetrieveAPIView().as_view(lookup_field='slug')(request, slug=slug)
        elif request.method == 'PATCH' or request.method == "PUT":
            return views.ProductUpdateAPIView().as_view(lookup_field='slug')(request, slug=slug)
        elif request.method == 'DELETE':
            return views.ProductDestroyAPIView().as_view(lookup_field='slug')(request, slug=slug)


    


