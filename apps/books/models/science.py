from django.db import models


class Science(models.Model):
    title = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.title)
