from django.db import models

class Usuario(models.Model):
    turma = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.turma})" if self.turma else self.username
