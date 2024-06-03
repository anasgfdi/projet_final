

import os
from django.db.models.signals import post_save
from django.dispatch import receiver
# from ..service.models import LogEntry
# from .tasks import process_log_file

# @receiver(post_save, sender=LogEntry)
# def log_entry_saved(sender, instance, **kwargs):
#     if instance.file_path:  # Vérifiez que l'instance a un chemin de fichier de logs
#         process_log_file(instance.file_path)


from django.contrib.auth.signals import user_logged_in, user_login_failed, user_logged_out
from django.dispatch import receiver
from .models import LoginActivity
from datetime import datetime

# @receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    current_datetime = datetime.now()
    action = f"L'utilisateur {user.username} est connecté"
    LoginActivity.objects.create(user=user, action=action, timestamp=current_datetime)

# @receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    current_datetime = datetime.now()
    action = f"Echec de connexion pour l'utilisateur {credentials.get('username', 'Inconnu')}"
    LoginActivity.objects.create(action=action, timestamp=current_datetime)

# @receiver(user_logged_out)
def log_user_login_logout(sender, request, user, **kwargs):
    current_datetime = datetime.now()
    action = f"L'utilisateur {user.username} s'est déconnecté"
    LoginActivity.objects.create(user=user, action=action, timestamp=current_datetime) 