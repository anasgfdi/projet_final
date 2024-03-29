from django import forms
from . import models

class PredictionForm(forms.ModelForm):

    class Meta:

        model = models.Features
        fields = '__all__'
        labels = {
            'age': 'Age du client',
            'housing': 'Qualité de logement du client ',
            'marital' :'Situation marietal du client',
            'job': "Emploi du client",
            'loan': "Le client possède t-il un prêt",
            'balance': "Solde du compte du client",
            'education':"Niveau de diplôme",
            'pdays': "Nombre de jours depuis le dernier contact du client lors d'une campagne précédente",
            'campaign': "Nombre de contacts effectués lors de cette campagne pour le client",
            'month': "Mois du dernier contact"
        }

