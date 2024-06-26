# Generated by Django 4.2.11 on 2024-05-06 09:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=18, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(18)])),
                ('housing', models.CharField(choices=[('1', 'yes'), ('0', 'no')], default=('1', 'yes'), max_length=3)),
                ('marital', models.CharField(choices=[('1', 'married'), ('0', 'single'), ('2', 'divorced')], default=('1', 'married'), max_length=3)),
                ('job', models.CharField(choices=[('0', 'admin.'), ('1', 'technician'), ('2', 'services'), ('3', 'management'), ('4', 'retired'), ('5', 'blue-collar'), ('6', 'unemployed'), ('7', 'entrepreneur'), ('8', 'housemaid'), ('9', 'unknown'), ('10', 'self-employed'), ('11', 'student')], default=('0', 'admin.'), max_length=80)),
                ('loan', models.CharField(choices=[('1', 'yes'), ('0', 'no')], default=('1', 'yes'), max_length=3)),
                ('balance', models.IntegerField(default=10000, null=True)),
                ('education', models.CharField(choices=[('0', 'primary'), ('1', 'secondary'), ('2', 'tertiary')], default=('0', 'primary'), max_length=80)),
                ('pdays', models.PositiveIntegerField(default=12, null=True)),
                ('campaign', models.PositiveIntegerField(default=1, null=True)),
                ('month', models.CharField(choices=[('0', 'sep.'), ('1', 'oct'), ('2', 'nov'), ('3', 'dec'), ('4', 'jan'), ('5', 'fev'), ('6', 'mar'), ('7', 'apr'), ('8', 'may'), ('9', 'jun'), ('10', 'jul'), ('11', 'aug')], default=('0', 'sep.'), max_length=9)),
            ],
        ),
        migrations.DeleteModel(
            name='ApiModel',
        ),
    ]
