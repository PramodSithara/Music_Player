from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name="MusicApp"

urlpatterns = [
    path('', views.log, name='log'),
    path('sign/', views.sign, name='sign'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),

]