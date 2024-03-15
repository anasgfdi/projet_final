from django.urls import path, include

from service import views

urlpatterns = [
    path('', views.services, name = 'services')
    
]
