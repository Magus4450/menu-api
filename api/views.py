from django.conf import settings
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from PIL import Image
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import models, serializers


class RestaurantListAPIView(generics.ListAPIView):

    queryset = models.Restaurant.objects.all()

    serializer_class = serializers.RestaurantSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'slug', 'location', 'status']

class RestaurantCreateAPIView(generics.CreateAPIView):

    queryset = models.Restaurant.objects.all()

    serializer_class = serializers.RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]

    
# class RestaurantListCreateAPIView(generics.ListCreateAPIView):

#     queryset = models.Restaurant.objects.all()
#     serializer_class = serializers.RestaurantSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['id', 'name', 'slug', 'location', 'status']

#     authentication_classes = [JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

class RestaurantRetrieveAPIView(generics.RetrieveAPIView):

    queryset = models.Restaurant.objects.all()

    serializer_class = serializers.RestaurantSerializer
    

class RestaurantUpdateAPIView(generics.UpdateAPIView):

    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]

class RestaurantDestroyAPIView(generics.DestroyAPIView):

    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = "DELETED"
        instance.save()
        data = {
            "status": "success",
        }
        return Response(data, status=status.HTTP_200_OK)


# class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Restaurant.objects.all()
#     serializer_class = serializers.RestaurantSerializer

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.status = "DELETED"
#         instance.save()
#         data = {
#             "status": "success",
#         }
#         return Response(data, status=status.HTTP_200_OK)
    
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

class CategoryListAPIView(generics.ListAPIView):

    queryset = models.Category.objects.all()

    serializer_class = serializers.CategorySerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'slug', 'restaurantId', 'status']


class CategoryCreateAPIView(generics.CreateAPIView):

    queryset = models.Category.objects.all()

    serializer_class = serializers.CategorySerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

# class CategoryListCreateAPIView(generics.ListCreateAPIView):
#     queryset = models.Category.objects.filter(
#         Q(status="ACTIVE") | Q(status="PENDING"))
#     serializer_class = serializers.CategorySerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['id', 'name', 'slug', 'restaurantId', 'status']

#     authentication_classes = [JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    
    queryset = models.Category.objects.all()

    serializer_class = serializers.CategorySerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CategoryUpdateAPIView(generics.UpdateAPIView):
    
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CategoryDestroyAPIView(generics.DestroyAPIView):
    
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = "DELETED"
        instance.save()
        data = {
            "status": "success",
        }
        return Response(data, status=status.HTTP_200_OK)


# class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Category.objects.all()
#     serializer_class = serializers.CategorySerializer

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.status = "DELETED"
#         instance.save()
#         data = {
#             "status": "success",
#         }
#         return Response(data, status=status.HTTP_200_OK)

#     authentication_classes = [JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]


class ProductListAPIView(generics.ListAPIView):

    queryset = models.Product.objects.all()

    serializer_class = serializers.ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'categoryId', 'restaurantId', 'price', 'status']

class ProductCreateAPIView(generics.CreateAPIView):

    queryset = models.Product.objects.all()

    serializer_class = serializers.ProductSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = models.Product.objects.filter(
#         Q(status="ACTIVE") | Q(status="PENDING"))
#     serializer_class = serializers.ProductSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['id', 'name', 'categoryId', 'restaurantId', 'price', 'status']

#     authentication_classes = [JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

class ProductRetrieveAPIView(generics.RetrieveAPIView):
    
    queryset = models.Product.objects.all()

class ProductUpdateAPIView(generics.UpdateAPIView):
    
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProductDestroyAPIView(generics.DestroyAPIView):
    
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = "DELETED"
        instance.save()
        data = {
            "status": "success",
        }
        return Response(data, status=status.HTTP_200_OK)

    
# class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Product.objects.all()
#     serializer_class = serializers.ProductSerializer

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.status = "DELETED"
#         instance.save()
#         data = {
#             "status": "success",
#         }
#         return Response(data, status=status.HTTP_200_OK)

#     authentication_classes = [JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
    
@api_view(['POST'])
def upload_image(request):
    image = request.data["image"]

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
