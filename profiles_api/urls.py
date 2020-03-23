from django.urls import path
from profiles_api import views

# for viewsets
from django.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', # URL
                views.HelloViewSet, # Class criada no arquivo views
                base_name = 'hello-viewset') # specifiing a base name



# Define API url for APIView
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), # for apiview
    path('', include(router.urls)), # for viewset - a string é blank pq eu não quero colocar nada no prefixo da URL
]
