# Generated by Django 4.2.11 on 2024-06-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('log_level', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
    ]
