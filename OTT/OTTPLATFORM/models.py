from django.db import models

# Create your models here.
class MovieProfile(models.Model):

    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    genres = models.CharField(max_length=100, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    main_actor = models.CharField(max_length=100, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)  # Duration in minutes
    image = models.ImageField(upload_to='Home/images/', blank=True, null=True)
    video = models.FileField(upload_to='Home/videos/', blank=True, null=True)
    is_disabled = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    

from django.db import models
from django.contrib.auth.hashers import make_password

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    password = models.CharField(max_length=128, null=True)
    subscription_plan = models.CharField(max_length=100, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    action = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)
