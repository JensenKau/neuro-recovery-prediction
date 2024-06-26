from __future__ import annotations

from django.db import models

from .user import User

class Patient(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    access = models.ManyToManyField(User, related_name="access", blank=True)
    
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    
    age = models.PositiveIntegerField(null=True)
    sex = models.CharField(max_length=10, choices={"male": "male", "female": "female"}, null=True)
    rosc = models.FloatField(null=True)
    ohca = models.BooleanField(null=True)
    shockable_rhythm = models.BooleanField(null=True)
    ttm = models.IntegerField(null=True)
    

if __name__ == "__main__":
    pass