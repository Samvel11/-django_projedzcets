from django.urls import path    # path - url sarqox funkcian a
from . import views
# from .views import home

urlpatterns = [
    path('', views.home, name="home"),
    path('messages',views.message_view, name="message_view"),
    path('home_view/',views.home_view, name="home_view"),
    path('register/',views.user_register, name="register"),

]