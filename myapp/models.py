from django.db import models
from django.urls import reverse


# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=255)
#     age = models.IntegerField()


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')

    # user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.created_at

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
