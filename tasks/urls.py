from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('save/', views.save, name='save'),

    #path('index/update', views.tasks, name='update_task'),
    
]

