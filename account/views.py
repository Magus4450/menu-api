
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.core.signing import Signer
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CustomUser, TokenValidation


@csrf_exempt
@api_view(http_method_names=['POST'])
def register_view(request):

    try:
        firstName = request.POST["firstName"]
    except:
        return Response({"message": "firstName is required!"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        lastName = request.POST["lastName"]
    except:
        return Response({"message": "lastName is required!"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        email = request.POST["email"]
    except:
        return Response({"message": "email is required!"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        password = request.POST["password"]
    except:
        return Response({"message": "password is required!"}, status=status.HTTP_400_BAD_REQUEST)


    user = CustomUser.objects.create(
        first_name=firstName,
        last_name=lastName,
        email=email,
        password=make_password(password),
        is_active=False,   
        restaurant_admin = True,
    )
    user.save()


    token = get_random_string(length=10).upper()

    # Hasing the User ID
    signer = Signer()
    uid = signer.sign_object(user.id)
    print(uid)

    send_mail(
        'Menu-App: Email Confirmation',
        f"""
        Please insert your token: {token} to confirm your email.\n

        OR click on the link below:
        http://localhost:3000/confirm-account/?userId={uid}&token={token}

        TEMPORARY LINK:
        http://localhost:8000/api/account/confirm/{uid}/{token}
        """,
        settings.APP_EMAIL,
        [email],
    )

    tv = TokenValidation.objects.create(
        userId = user,
        email = email,
        token = token,        
    )

    tv.save()

    return Response(
        {"message": "Token has been sent to the email"},
        status=status.HTTP_200_OK
    )

@api_view(http_method_names=['POST', 'GET'])
def confirm_token(request, userId, token):
    if request.method == 'POST':
        try:
            token = request.POST["token"]
        except:
            return Response({"message": "token is required!"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            userId = request.POST["userId"]
        except:
            return Response({"message": "userId is required!"}, status=status.HTTP_400_BAD_REQUEST)
   

    try:
        userId = int(userId)
    except:
        signer = Signer()
        userId = signer.unsign_object(userId)

    try:
        tv = TokenValidation.objects.get(userId=userId)
        user = tv.userId
    except:
        return Response({"message": "userId is invalid!"}, status=status.HTTP_400_BAD_REQUEST)

    if tv.timeTried >= 3:
        # tv.delete()
        return Response({"message": "You have exceeded the limit of attempts!"}, status=status.HTTP_400_BAD_REQUEST)

    if tv.token == token:
        user.is_active = True
        user.save()
        # tv.delete()
        return Response({"message": "Email has been confirmed"}, status=status.HTTP_200_OK)
    else:
        tv.timeTried += 1
        tv.save()
        return Response({"message": "Token is invalid"}, status=status.HTTP_400_BAD_REQUEST)

