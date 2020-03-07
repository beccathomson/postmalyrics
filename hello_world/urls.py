from django.urls import path
from hello_world import views
from django.conf.urls import url

urlpatterns = [
    path('', views.hello_world, name='hello_world'), # for helloworld.html
    path('search_lyrics', views.search_lyrics, name='search_lyrics')
]