from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.state.name + ' - ' + self.name

