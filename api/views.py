from . import models
from django.db.models import Q
from rest_framework import generics
from . import serializers

class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    # Filter by status
    queryset = models.Restaurant.objects.filter(Q(status="ACTIVE") | Q(status="PENDING"))
    serializer_class = serializers.RestaurantSerializer
    


class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer

    def destroy(self):
        instance = self.get_object()
        instance.status = "DELETED"
        instance.save()
        data = {
            "status": "success",
        }
        return Response(data, status=status.HTTP_200_OK)
        

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Category.objects.filter(Q(status="ACTIVE") | Q(status="PENDING"))
    serializer_class = serializers.CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def destroy(self):
        instance = self.get_object()
        instance.status = "DELETED"
        instance.save()
        data = {
            "status": "success",
        }
        return Response(data, status=status.HTTP_200_OK)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.filter(Q(status="ACTIVE") | Q(status="PENDING"))
    serializer_class = serializers.ProductSerializer




class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def destroy(self):
        instance = self.get_object()
        instance.status = "DELETED"
        instance.save()
        data = {
            "status": "success",
        }
        return Response(data, status=status.HTTP_200_OK)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
from django.conf import settings

@api_view(['POST'])
def upload_image(request):
    image = request.data["image"]

    try:
        type = request.data["type"]
    except:
        type = "image"

    import os
    ROOT_URL = settings.MEDIA_ROOT
    print(ROOT_URL)
    FINAL_URL = os.path.join(ROOT_URL, type)

    if not os.path.exists(FINAL_URL):
        os.makedirs(FINAL_URL)
    

    im = Image.open(image.temporary_file_path())
    
    from django.utils import timezone
    
    time = str(timezone.now().strftime("%Y%m%d%H%M%S"))
    split = image.name.split(".")
    name = "".join(split[:-1])
    format = split[-1]
    image_name = f"{name}{time}.{format}"
    # image_name = image.name.replace(image.format, "") + time + "." + image.format
    IMG_URL = os.path.join(FINAL_URL, image_name)


    im = im.save(IMG_URL)
    print(ROOT_URL.replace("\\media",""))
    print(IMG_URL)
    imageUrl = IMG_URL.replace(ROOT_URL.replace("\\media",""),"")
    data = {
        "imageUrl": imageUrl
    }
    print(imageUrl)
    return Response(data, status=status.HTTP_200_OK)


    



