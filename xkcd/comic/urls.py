from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('previous/<int:pk>', views.previous, name='previous'),
   
]
