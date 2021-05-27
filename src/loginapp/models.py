from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics', )
    description = models.TextField(blank=True)
    dob = models.DateField(blank=True, null=True, )
    website = models.URLField(blank=True, null=True, )
    facebook = models.URLField(blank=True, null=True, )

    def __str__(self):
        return self.name


class Follow(models.Model):
    follower = models.ForeignKey(User, models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, models.CASCADE, related_name='following')


    



