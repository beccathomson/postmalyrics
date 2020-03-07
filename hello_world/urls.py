from django.urls import path
from hello_world import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'), # for initial load (?)
    # path('search_lyrics', views.search_lyrics, name='search_lyrics')
]