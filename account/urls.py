from django.urls import path
from . import views
urlpatterns = [
    path('account/register/', views.register_view),
    path('account/confirm/', views.confirm_token),

]