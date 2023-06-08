from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserCreationForm
from django.forms.utils import ErrorDict
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email

        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer







@api_view(['POST'])
def Send_Message(request):
    if request.method=='POST':
        body=request.data.get('body')
        gmail=request.data.get('gmail')
        fullname=request.data.get('fullname')
        phone=request.data.get('phone')
        body= "message from "+ fullname + " with the phone "+ phone +" and the message : "+body
        try:
            send_mail(fullname, body, settings.EMAIL_HOST_USER, [gmail])
        except:
            return Response("email not send...")

        return Response("success")

@api_view(['POST'])
def register(request):
    register_data = CustomUserCreationForm(request.data)
    
    if register_data.is_valid():
        register_data.save()
        return Response("Account created")
    else:
        error_messages = {}
        for field, errors in register_data.errors.items():
            error_messages[field] = [str(error) for error in errors]

        return Response({"errors": error_messages}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password1')
    print(username + password)

    # Authenticate user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response('Login successful')
    # Return an error response if authentication fails
    return Response('Invalid login credentials')