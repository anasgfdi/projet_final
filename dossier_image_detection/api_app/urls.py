from django.urls import path
from . import views

app_name = "api_app"

urlpatterns = [
    path('', views.api, name= "api_app")
]


from django.urls import path # Import du module Path  
from .views import * # Import de notre fichier views

# urlpatterns = [
#     # path("", accueil, name="home"),
#     path("questionnaire/", home_view, name="questionnaire")]