from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, models.CASCADE, related_name='post_author', blank=True, null=True, )
    image = models.ImageField(upload_to='post_images')
    caption = models.CharField(max_length=263, blank=True, )
    upload_date = models.DateTimeField(auto_now_add=True, )
    update_date = models.DateTimeField(auto_now=True, )

    class Meta:
        ordering = ('-upload_date', )

class Like(models.Model):
    post = models.ForeignKey(Post, models.CASCADE, related_name='liked_post', null=True, blank=True, )
    user = models.ForeignKey(User, models.CASCADE, related_name='liker')
    created_date = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return '{} : {}'.format(self.user, self.post)