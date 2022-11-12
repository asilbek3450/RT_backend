from django.db import models


# Create your models here.

class Science(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False, unique=True)

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
    science1 = models.ForeignKey(Science, on_delete=models.CASCADE, null=False, blank=False, related_name='science1')
    science2 = models.ForeignKey(Science, on_delete=models.CASCADE, null=False, blank=False, related_name='science2')
<<<<<<< HEAD
    language_id = models.ForeignKey("users.LanguageChoices", on_delete=models.CASCADE, null=False, blank=False)
=======
    language_id = models.ForeignKey("users.LanguageChoices", on_delete=models.CASCADE, null=True, blank=True)
>>>>>>> 3702e74f09e38eacde3501e99e2aab301d651d8e
    book_type = models.ForeignKey("books.BookType", on_delete=models.CASCADE, null=True, blank=True)
    is_free = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
<<<<<<< HEAD
        return f'{self.id} {self.science1.title} - {self.science2.title}'
=======
        return f'{str(self.id)} {str(self.science1)} - {str(self.science2)}'
>>>>>>> 3702e74f09e38eacde3501e99e2aab301d651d8e
