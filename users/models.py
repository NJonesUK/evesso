from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import logging

logger = logging.getLogger("custom")
  
class UserProfile(models.Model):
    # self field is required.
    user = models.OneToOneField(User)

    # Other fields here    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
post_save.connect(create_user_profile, sender=User)