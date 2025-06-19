from django.db import models
from django.contrib.auth.models import User


class FamilyGroup(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Family")


class Child(models.Model):
    family = models.ForeignKey(FamilyGroup, on_delete=models.CASCADE, related_name="children")
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
