from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

urlpatterns = [
    path('account/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('account/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('account/register/', views.RegisterAPIView.as_view()),
    path('account/confirm/', views.ConfirmTokenPOSTAPIView.as_view()),
    path('account/confirm/<str:userId>/<str:token>', views.ConfirmTokenGETAPIView.as_view()),

]
