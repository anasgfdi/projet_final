import pytest
from django.urls import reverse
from django.test import Client
from unittest.mock import patch
from api_app.forms import PredictionForm
from api_app.models import Features

@pytest.mark.django_db
class TestApiView:

    @pytest.fixture
    def client(self):
        return Client()

    def test_api_get(self, client):
        response = client.get(reverse('api'))
        assert response.status_code == 200
        assert 'form' in response.context
        assert isinstance(response.context['form'], PredictionForm)

    @patch('api_app.views.requests.post')
    def test_api_post_valid(self, mock_post, client):
        mock_post.return_value.text = '0'
        data = {
            'age': 30,
            'housing': 'owner',
            'marital': 'single',
            'job': 'admin',
            'loan': 'no',
            'balance': 1500,
            'education': 'university',
            'pdays': 5,
            'campaign': 1,
            'month': 'may'
        }
        response = client.post(reverse('api'), data)
        assert response.status_code == 200
        assert "Félicitations votre prêt a été accordé !" in response.content.decode()

    @patch('api_app.views.requests.post')
    def test_api_post_invalid(self, mock_post, client):
        data = {
            'age': '18',  # Champ manquant ou invalide
            'housing': 'owner',
            'marital': 'single',
            'job': 'admin',
            'loan': 'no',
            'balance': 1500,
            'education': 'university',
            'pdays': 5,
            'campaign': 1,
            'month': 'may'
        }
        response = client.post(reverse('api'), data)
        assert response.status_code == 200
        assert 'form' in response.context
        assert isinstance(response.context['form'], PredictionForm)
        assert not response.context['form'].is_valid()
