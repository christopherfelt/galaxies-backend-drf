from django.db import models
from galaxies.models import Galaxy

class Star(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    galaxy_id = models.ForeignKey(Galaxy, related_name="stars", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name