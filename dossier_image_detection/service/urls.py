from django.urls import path, include

from service import views

urlpatterns = [
    # path('', views.services, name = 'services'),
    # path('', views.log_list, name='log_list'),
    path('', views.login_activity, name='log_list')
    
]

