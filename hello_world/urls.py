from django.urls import path
from hello_world import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('', views.hello_world, name='get_lyrics'),
    path(r'^signup', views.signup, name='signup'),
]