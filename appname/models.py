from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(blank=True,null=True,unique=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/',default='default.png')
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    phone = models.CharField(max_length=15,blank=True,null=True,default="none")
    country=models.CharField(max_length=100,blank=True,null=True,default="none")
    city=models.CharField(max_length=100,blank=True,null=True,default="none")

    def __str__(self):
        return str(self.email)
