from django import forms
from . import models

class PredictionForm(forms.ModelForm):

    class Meta:

        model = models.Features
        fields = '__all__'
        labels = {
            'Industry': 'Choissisez le domaine de votre entreprise',
            'Term': 'Entrez le temps accordé pour rembourser (en mois)',
            'GrAppv' :'Entrez le montant accordé par votre banque',
            'NoEmp': "Entrez le nombre d'employés dans votre entreprise",
            'NewExist': "Veuillez choisir la catégorie de votre entreprise",
            'CreateJob': "Entrez le nombre d'emplois crées",
            'RetainedJob':"Entrez le nombre d'emplois préservés",
            'FranchiseCode': "Entrez le numéro de votre Entreprise",
            'UrbanRural': "Etes vous dans une zone urbaine ou rural ?",
            'Real_estate': "Est ce que vous possédez un patrimoine immobilier ?"
        }

class StateForm(forms.ModelForm) :
    class Meta:
        model = models.State
        fields = '__all__'
        labels={ 'State' : 'Choissisez  la localisation de votre entreprise'}
