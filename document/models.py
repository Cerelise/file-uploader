from django.db import models


class Document(models.Model):
    document = models.FileField(upload_to='uploads/')

    def __str__(self):
        return str(self.pk)
