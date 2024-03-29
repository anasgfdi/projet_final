from django.db import models
import pandas as pd
from django.core.validators import MaxValueValidator,MinValueValidator

df = pd.read_csv('data.csv') 

choix_1 = [
    ('1', 'yes'),
    ('0', 'no'),
]

choix_2 = [
    ('1', 'married'),
    ('0', 'single'),
    ('2','divorced')
]


choix_3=[('0','admin.'),
        ('1','technician'),
        ('2','services'),
        ('3','management'),
        ('4','retired'),
        ('5','blue-collar'), 
        ('6','unemployed'),
        ('7','entrepreneur'),
        ('8','housemaid'),
        ('9','unknown'),
        ('10','self-employed'),
        ('11','student')
]

choix_4=[('0','sep.'),
        ('1','oct'),
        ('2','nov'),
        ('3','dec'),
        ('4','jan'),
        ('5','fev'), 
        ('6','mar'),
        ('7','apr'),
        ('8','may'),
        ('9','jun'),
        ('10','jul'),
        ('11','aug')
]

choix_5=[
    ('0','primary'),
    ('1','secondary'),
    ('2','tertiary')
]

class Features(models.Model):
    age = models.IntegerField(null=False, validators=[MaxValueValidator(100),MinValueValidator(18)],default=18)
    housing = models.CharField(max_length=3, choices=choix_1, default=choix_1[0])
    marital = models.CharField(max_length=3, choices=choix_2, default=choix_2[0])
    job = models.CharField(max_length=80, choices=choix_3, default=choix_3[0])
    loan=models.CharField(max_length=3, choices=choix_1, default=choix_1[0])
    balance = models.IntegerField(null=True, default=10000)
    education = models.CharField(max_length=80, choices=choix_5, default=choix_5[0])
    pdays = models.PositiveIntegerField(null=True, default=12)
    campaign=models.PositiveIntegerField(null=True, default=1)
    month = models.CharField(max_length=9, choices=choix_4, default=choix_4[0])
