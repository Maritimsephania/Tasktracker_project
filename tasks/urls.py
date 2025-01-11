from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('index/add', views.tasks, name='add_task'),
    path('index/update', views.tasks, name='update_task'),
    
]

