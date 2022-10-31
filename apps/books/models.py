from django.db import models


# Create your models here.

class Science(models.Model):
    title = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class BookType(models.Model):
    title = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.title)


class Book(models.Model):
    science1 = models.ForeignKey(Science, on_delete=models.CASCADE, null=True, blank=True, related_name='science1')
    science2 = models.ForeignKey(Science, on_delete=models.CASCADE, null=True, blank=True, related_name='science2')
    language_id = models.ForeignKey("users.LanguageChoices", on_delete=models.CASCADE, null=True, blank=True)
    book_type = models.ForeignKey("books.BookType", on_delete=models.CASCADE, null=True, blank=True)
    is_free = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)
