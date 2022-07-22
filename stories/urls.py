from . import views
from django.urls import path


urlpatterns = [
    path('', views.StoryList.as_view(), name='home'),
    path('', views.HeadlineList.as_view(), name='home')
]