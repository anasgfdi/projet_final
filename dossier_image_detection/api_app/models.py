from django.db import models
import pandas as pd
from django.core.validators import MaxValueValidator,MinValueValidator

df = pd.read_csv('data.csv') 

choix_1 = [
    ('yes', 'yes'),
    ('no', 'no'),
]

choix_2 = [
    ('married', 'married'),
    ('single', 'single'),
    ('divorced','divorced')
]


choix_3=[('admin.','admin.'),
        ('technician','technician'),
        ('services','services'),
        ('management','management'),
        ('retired','retired'),
        ('blue-collar','blue-collar'), 
        ('unemployed','unemployed'),
        ('entrepreneur','entrepreneur'),
        ('housemaid','housemaid'),
        ('unknown','unknown'),
        ('self-employed','self-employed'),
        ('student','student')
]

choix_4=[('sep','sep.'),
        ('oct','oct'),
        ('nov','nov'),
        ('dec','dec'),
        ('jan','jan'),
        ('fev','fev'), 
        ('mar','mar'),
        ('apr','apr'),
        ('may','may'),
        ('jun','jun'),
        ('jul','jul'),
        ('aug','aug')
]

choix_5=[
    ('primary','primary'),
    ('secondary','secondary'),
    ('tertiary','tertiary')
]

class Features(models.Model):
    age = models.IntegerField(null=False, validators=[MaxValueValidator(100),MinValueValidator(18)],default=18)
    housing = models.CharField(max_length=30, choices=choix_1, default=choix_1[0])
    marital = models.CharField(max_length=30, choices=choix_2, default=choix_2[0])
    job = models.CharField(max_length=80, choices=choix_3, default=choix_3[0])
    loan=models.CharField(max_length=30, choices=choix_1, default=choix_1[0])
    balance = models.IntegerField(null=True, default=10000)
    education = models.CharField(max_length=80, choices=choix_5, default=choix_5[0])
    pdays = models.PositiveIntegerField(null=True, default=12)
    campaign=models.PositiveIntegerField(null=True, default=1)
    month = models.CharField(max_length=90, choices=choix_4, default=choix_4[0])
