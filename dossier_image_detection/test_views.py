import pytest
from django.urls import reverse
from django.test import Client
from unittest.mock import patch
from api_app.forms import PredictionForm
from api_app.models import Features

# @pytest.mark.django_db
# class TestApiView:

#     @pytest.fixture
#     def client(self):
#         return Client()

#     def test_api_get(self, client):
#         response = client.get(reverse('api'))
#         assert response.status_code == 200
#         assert 'form' in response.context
#         assert isinstance(response.context['form'], PredictionForm)

#     @patch('api_app.views.requests.post')
#     def test_api_post_valid(self, mock_post, client):
#         mock_post.return_value.text = '0'
#         data = {
#             'age': 30,
#             'housing': 'owner',
#             'marital': 'single',
#             'job': 'admin',
#             'loan': 'no',
#             'balance': 1500,
#             'education': 'university',
#             'pdays': 5,
#             'campaign': 1,
#             'month': 'may'
#         }
#         response = client.post(reverse('api'), data)
#         assert response.status_code == 200
#         assert "Félicitations votre prêt a été accordé !" in response.content.decode()

#     @patch('api_app.views.requests.post')
#     def test_api_post_invalid(self, mock_post, client):
#         data = {
#             'age': '18',  # Champ manquant ou invalide  
#             'housing': 'owner',
#             'marital': 'single',
#             'job': 'admin',
#             'loan': 'no',
#             'balance': 1500,
#             'education': 'university',
#             'pdays': 5,
#             'campaign': 1,
#             'month': 'may'
#         }
#         response = client.post(reverse('api'), data)
#         assert response.status_code == 200
#         assert 'form' in response.context
#         assert isinstance(response.context['form'], PredictionForm)
#         assert not response.context['form'].is_valid()
import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_homepage_view():
    client = Client()
    
    # Obtenez l'URL de la vue 'homepage'
    url = reverse('home')
    
    # Faites une requête GET à cette URL
    response = client.get(url)
    
    # Vérifiez que la réponse HTTP est 200 OK
    assert response.status_code == 200
    
    # Vérifiez que le template correct est utilisé
    assert 'home_page.html' in [t.name for t in response.templates]
    

# tests/test_urls.py
from django.urls import resolve, reverse

class TestUrls:
    def test_admin_url(self):
        """
        Test admin URL resolves to admin view.
        """
        url = reverse('admin:index')
        assert resolve(url).view_name == 'admin:index'

    def test_homepage_url(self):
        """
        Test homepage URL resolves to homepage view.
        """
        url = reverse('home')
        assert resolve(url).func == homepage  # Assuming `homepage` is imported correctly

    def test_api_url(self):
        """
        Test API URL resolves to api_app view.
        """
        url = reverse('api')
        assert resolve(url).func.view_class == ApiView  # Assuming the view class name is `ApiView`

    def test_signup_url(self):
        """
        Test signup URL resolves to signup view.
        """
        url = reverse('signup')
        assert resolve(url).func.view_class == SignupView  # Assuming the view class name is `SignupView`

    def test_logs_url(self):
        """
        Test logs URL resolves to service view.
        """
        url = reverse('logs')
        assert resolve(url).func.view_class == ServiceView  # Assuming the view class name is `ServiceView`

    def test_accounts_url(self):
        """
        Test accounts URL resolves to Django authentication views.
        """
        url = reverse('django.contrib.auth.urls')
        assert resolve(url).func.view_class == AuthenticationView  # Assuming the view class name is `AuthenticationView`
