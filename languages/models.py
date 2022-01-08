from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.name} -- {self.paradigm}'
