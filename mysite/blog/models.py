from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Voetbalspelers(models.Model):
    naam = models.CharField(max_length=200)
    actuele_club = models.CharField(max_length=200)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    datum_invoer = models.DateTimeField(default=timezone.now)
    datum_laatste_aanpassing = models.DateTimeField(auto_now=True)

    def publish(self):
        """Slaat het object op (zoals bij het Post-model)."""
        self.save()

    def __str__(self):
        return self.naam