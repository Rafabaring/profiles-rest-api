from django.urls import path

from profiles_api import views

urlpatterns = [
    path('hellop-view/', views.HelloApiView.as_view()),
]
