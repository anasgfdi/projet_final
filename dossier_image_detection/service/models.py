from django.db import models

# # Create your models here.
# # myapp/models.py

# from django.db import models

# class LogEntry(models.Model):
#     timestamp = models.DateTimeField()
#     log_level = models.CharField(max_length=10)
#     message = models.TextField()

#     def __str__(self):
#         return f"{self.timestamp} - {self.log_level} - {self.message}"


# myapp/models.py

from django.db import models
from django.contrib.auth.models import User

class LoginActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.timestamp} - {self.user.username if self.user else 'Inconnu'} - {self.action}"
