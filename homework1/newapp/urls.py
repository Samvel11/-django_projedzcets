from django.urls import path
from .views import hello,about, start, time,square 

urlpatterns = [
    path('', start),
    path('about',about),
    path('greeting', hello),
    path('date', time),
    path('dict', square)
]
