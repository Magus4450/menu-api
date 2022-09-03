from urllib import request

import coreapi
import coreschema
from django.conf import settings
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from PIL import Image
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import models, serializers


class RestaurantListCreateAPIView(generics.ListCreateAPIView):

    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'slug', 'location', 'status']

    
    def get_authenticators(self):
        # If the request method is GET, no auth needed
        if self.request:
            if self.request.method == 'POST':
                self.authentication_classes = [JWTAuthentication]  
                self.permission_classes = [permissions.IsAuthenticated]
            else:
                self.authentication_classes = []  
                self.permission_classes = []
        return super().get_authenticators()

class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'slug', 'location', 'status']

    def get_authenticators(self):
        # If the request method is GET, no auth needed
        if self.request:
            if self.request.method in ['DELETE', 'PUT', 'PATCH']:
                self.authentication_classes = [JWTAuthentication]  
                self.permission_classes = [permissions.IsAuthenticated]
            else:
                self.authentication_classes = []  
                self.permission_classes = []
        return super().get_authenticators()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = "DELETED"
        instance.save()
        data = {
            "status": "success",
        }
        return Response(data, status=status.HTTP_200_OK)

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'slug', 'restaurantId', 'status']

    def get_authenticators(self):
        # If the request method is GET, no auth needed
        if self.request:
            if self.request.method == 'POST':
                self.authentication_classes = [JWTAuthentication]  
                self.permission_classes = [permissions.IsAuthenticated]
            else:
                self.authentication_classes = []  
                self.permission_classes = []
        return super().get_authenticators()

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'slug', 'restaurantId', 'status']

    def get_authenticators(self):
        # If the request method is GET, no auth needed
        if self.request:
            if self.request.method in ['DELETE', 'PUT', 'PATCH']:
                self.authentication_classes = [JWTAuthentication]  
                self.permission_classes = [permissions.IsAuthenticated]
            else:
                self.authentication_classes = []  
                self.permission_classes = []
        return super().get_authenticators()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = "DELETED"
        instance.save()
        data = {
            "status": "success",
        }
        return Response(data, status=status.HTTP_200_OK)


class ProductListCreateAPIView(generics.ListCreateAPIView):
        
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'restaurantId', 'categoryId', 'status']

    def get_authenticators(self):
        # If the request method is GET, no auth needed
        if self.request:
            if self.request.method == 'POST':
                self.authentication_classes = [JWTAuthentication]  
                self.permission_classes = [permissions.IsAuthenticated]
            else:
                self.authentication_classes = []  
                self.permission_classes = []
        return super().get_authenticators()

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'restaurantId', 'categoryId', 'status']

    def get_authenticators(self):
        # If the request method is GET, no auth needed
        if self.request:
            if self.request.method in ['DELETE', 'PUT', 'PATCH']:
                self.authentication_classes = [JWTAuthentication]  
                self.permission_classes = [permissions.IsAuthenticated]
            else:
                self.authentication_classes = []  
                self.permission_classes = []
        return super().get_authenticators()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = "DELETED"
        instance.save()
        data = {
            "status": "success",
        }
        return Response(data, status=status.HTTP_200_OK)



    

class UploadAPIView(generics.GenericAPIView):

    serializer_class = serializers.UploadSerializer

    def post(self, request):
        image = request.data["image"]
        if type(image) == str:
            return Response({"status": "error", "message": "Invalid image type"}, status=status.HTTP_400_BAD_REQUEST)

        # If type not specified set type to image
        try:
            type_img = request.data["type"]
        except:
            type_img = "image"

        import os

        from django.utils import timezone

        # Access media root url
        ROOT_URL = settings.MEDIA_ROOT
        # Add type name to media root
        FINAL_URL = os.path.join(ROOT_URL, type_img)

        # Create directory of type if doesnt exist
        if not os.path.exists(FINAL_URL):
            os.makedirs(FINAL_URL)


        # Get current time
        time = str(timezone.now().strftime("%Y%m%d%H%M%S"))

        # Getting image name and format
        split = image.name.split(".")
        name = "".join(split[:-1])
        format = split[-1]

        if format not in ["jpg", "jpeg", "png"]:
            return Response({"status": "error", "message": "Format not supported"}, status=status.HTTP_400_BAD_REQUEST)

        # Finaly image name after adding time and format
        image_name = f"{name}{time}.{format}"

        IMG_URL = os.path.join(FINAL_URL, image_name)

        from django.core.files import uploadedfile

        # Check if image is either InMemoryUploadedFile or TemporaryUploadedFile

        if isinstance(image, uploadedfile.InMemoryUploadedFile):
            
            # Save from memory to disk
            with open(IMG_URL, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
        
        elif isinstance(image, uploadedfile.TemporaryUploadedFile):
        
            im = Image.open(image.temporary_file_path())
            im = im.save(IMG_URL)


        # Configuring response url
        if "\\media" in ROOT_URL:
            ROOT_URL = ROOT_URL.replace("\\media", "")
        imageUrl = IMG_URL.replace(ROOT_URL, "")
        data = {
            "imageUrl": imageUrl
        }
        
        return Response(data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def upload_image(request):
#     image = request.data["image"]

#     # If type not specified set type to image
#     try:
#         type_img = request.data["type"]
#     except:
#         type_img = "image"

#     import os

#     from django.utils import timezone

#     # Access media root url
#     ROOT_URL = settings.MEDIA_ROOT
#     # Add type name to media root
#     FINAL_URL = os.path.join(ROOT_URL, type_img)

#     # Create directory of type if doesnt exist
#     if not os.path.exists(FINAL_URL):
#         os.makedirs(FINAL_URL)


#     # Get current time
#     time = str(timezone.now().strftime("%Y%m%d%H%M%S"))

#     # Getting image name and format
#     split = image.name.split(".")
#     name = "".join(split[:-1])
#     format = split[-1]

#     # Finaly image name after adding time and format
#     image_name = f"{name}{time}.{format}"

#     IMG_URL = os.path.join(FINAL_URL, image_name)

#     from django.core.files import uploadedfile

#     # Check if image is either InMemoryUploadedFile or TemporaryUploadedFile

#     if isinstance(image, uploadedfile.InMemoryUploadedFile):
        
#         # Save from memory to disk
#         with open(IMG_URL, 'wb+') as destination:
#             for chunk in image.chunks():
#                 destination.write(chunk)
       
#     elif isinstance(image, uploadedfile.TemporaryUploadedFile):
       
#         im = Image.open(image.temporary_file_path())
#         im = im.save(IMG_URL)


#     # Configuring response url
#     if "\\media" in ROOT_URL:
#         ROOT_URL = ROOT_URL.replace("\\media", "")
#     imageUrl = IMG_URL.replace(ROOT_URL, "")
#     data = {
#         "imageUrl": imageUrl
#     }
    
#     return Response(data, status=status.HTTP_200_OK)
