from django.contrib import admin
from .models import Song, user

# Register your models here.
admin.site.register(Song)
admin.site.register(user)