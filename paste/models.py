from django.db import models

class Paste(models.Model):
    url = models.CharField(max_length=128)
    content = models.TextField()

    def __str__(self):
        return self.url
