from django.urls import path
from . import views

# NB: app_name do distinguish names betweens apps
# movie_detail => movieapp:movie_detail
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:id>', views.movie_detail, name='movie_detail'),
    path('search', views.movie_search, name='movie_search'),
    path('add', views.MovieCreate.as_view(), name='movie_add'),
    path('<int:pk>/edit', views.MovieUpdate.as_view(), name='movie_update'),

    # misc/demo
    path('demo1', views.demo_http_response, name='demo1'),
    path('demo2', views.demo_bad_request, name='demo2'),
]