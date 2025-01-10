from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('index/add', views.tasks, name='tasks'),
    path('index/update', views.index, name='update_task'),
    
]

