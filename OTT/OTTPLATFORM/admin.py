from django.contrib import admin
from .models import UserProfile, MovieProfile

# Register your models here.

admin.site.register(MovieProfile)
admin.site.register(UserProfile)

