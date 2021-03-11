from django.urls import path
from .views import homePageView,HomePageView,CreatePageView


urlpatterns=[
    # path("", homePageView),
    path("/", HomePageView.as_view()),
    path("about/", CreatePageView.as_view())
]
