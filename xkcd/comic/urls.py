from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('previous/', views.previous, name='previous'),
    path('next/', views.next, name='next'),
    path('test/',views.test_page, name="test_page")
   
]
