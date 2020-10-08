from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=90)
    username = models.CharField(max_length=60)

    def __str__(self):
        return self.name
