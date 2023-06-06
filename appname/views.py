from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserCreationForm
# Create your views here.


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
    register_data = UserCreationForm(request.POST)
    if register_data.is_valid():
        register_data.save()
        return Response("Account created")
    else:
        return Response("Invalid data")
    
    

