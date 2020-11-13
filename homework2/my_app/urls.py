from django.urls import path
from . import views



urlpatterns = [
    path('json',views.json_read, name='json_read'),
    path('',views.main_html, name='file'),
    path('task',views.task, name='task'),

]
