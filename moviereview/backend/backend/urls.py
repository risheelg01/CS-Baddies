from django.urls import path
from . import views

urlpatterns = [
    path('movie_review/<str:movie_name>/', views.movie_review_view, name='movie_review'),
]