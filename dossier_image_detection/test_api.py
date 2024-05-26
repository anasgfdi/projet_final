from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
import json
from .forms import PredictionForm

class ApiViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('api')  # Assurez-vous que le nom de votre vue est 'api'

    def test_api_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')
        self.assertIsInstance(response.context['form'], PredictionForm)

    @patch('requests.post')
    def test_api_post_valid_form(self, mock_post):
        mock_post.return_value.text = '0'
        form_data = {
            'age': 35,
            'housing': 'own',
            'marital': 'married',
            'job': 'admin.',
            'loan': 'no',
            'balance': 1500,
            'education': 'university.degree',
            'pdays': 999,
            'campaign': 1,
            'month': 'may'
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'result.html')
        self.assertIn('Félicitations votre prêt a été accordé !', response.content.decode())

    @patch('requests.post')
    def test_api_post_invalid_form(self, mock_post):
        form_data = {
            'age': '',
            'housing': 'own',
            'marital': 'married',
            'job': 'admin.',
            'loan': 'no',
            'balance': 1500,
            'education': 'university.degree',
            'pdays': 999,
            'campaign': 1,
            'month': 'may'
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')
        self.assertIsInstance(response.context['form'], PredictionForm)

    @patch('requests.post')
    def test_api_post_rejected_application(self, mock_post):
        mock_post.return_value.text = '1'
        form_data = {
            'age': 35,
            'housing': 'own',
            'marital': 'married',
            'job': 'admin.',
            'loan': 'no',
            'balance': 1500,
            'education': 'university.degree',
            'pdays': 999,
            'campaign': 1,
            'month': 'may'
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'result.html')
        self.assertIn("Malheureusement votre dossier n'a pas été retenu , une prochaine fois peut-être", response.content.decode())

    @patch('requests.post')
    def test_api_post_request_error(self, mock_post):
        mock_post.return_value.status_code = 500  # Simuler une erreur du serveur
        form_data = {
            'age': 35,
            'housing': 'own',
            'marital': 'married',
            'job': 'admin.',
            'loan': 'no',
            'balance': 1500,
            'education': 'university.degree',
            'pdays': 999,
            'campaign': 1,
            'month': 'may'
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')
        self.assertIn('Une erreur est survenue lors du traitement de votre demande', response.content.decode())
