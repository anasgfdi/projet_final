# # myapp/models.py

# from django.db import models
# from django.contrib.auth.models import User

# class LoginActivity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     action = models.CharField(max_length=255)
#     timestamp = models.DateTimeField()

#     def __str__(self):
#         return f"{self.timestamp} - {self.user.username if self.user else 'Inconnu'} - {self.action}"
