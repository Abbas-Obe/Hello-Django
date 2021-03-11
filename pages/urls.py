from django.urls import path
from .views import homePageView, home, ourPost


urlpatterns=[
    path("", homePageView),
    path("abbas", home),
    path("abbas/second", ourPost)
]
