from django.urls import path
from . import views

# NB: app_name do distinguish names betweens apps
# movie_detail => movieapp:movie_detail
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:id>', views.movie_detail, name='movie_detail'),
]