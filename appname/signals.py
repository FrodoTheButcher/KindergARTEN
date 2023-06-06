from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings




#cand stergem un profil stergem un user
def deleteProfile(sender,instance,**kwargs):
    user = instance.owner
    user.delete()

#create/update profile cand cream/updatam un user
def UserCreate(sender,instance,created,**kwargs):
    user = instance 

    if created:
        profile = Profile.objects.create(
            owner=user,
            username=user.username
        )
        send_mail(
        "Account created  "+ user.first_name,
        "Succesfully created the account",
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
        )
    else:
        profile = Profile.objects.get(owner=user)
        profile.username=instance.username
        profile.name=instance.first_name
        profile.last_name=instance.last_name
        profile.email=instance.email
        profile.save()


post_delete.connect(deleteProfile,sender=Profile)
post_save.connect(UserCreate,sender=User)