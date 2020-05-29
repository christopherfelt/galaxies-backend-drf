from django.db import models


class Galaxy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name