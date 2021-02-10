from django.db import models

class NPC(models.Model):
  name = models.CharField(max_length=100)
  race = models.CharField(max_length=100)
  is_advent = models.BooleanField()
  role = models.CharField(max_length=100, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
