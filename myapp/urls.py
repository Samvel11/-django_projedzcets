from django.urls import path
from .views import home, name

app_name = 'myapp'
urlpatterns = [
    path('home/', home, name="home" ),
    path('name/', name, name="name" ), 
]