from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'last_name', 'profile_image', 'username', 'email','city','country','phone']
