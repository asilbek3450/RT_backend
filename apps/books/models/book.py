from django.db import models

from books.models.science import Science


# TypeBooks = (
#     ('0', 'Theme Test'),
#     ('1', 'Block Test'),
#     ('2', 'Attestation Test'),
#     ('3', 'Online Test'),
# )

class BookType(models.Model):
    title = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.title)


class Book(models.Model):

    science1 = models.ManyToManyField(Science)
    science2 = models.ManyToManyField(Science)
    language_id = models.ForeignKey("users.LanguageChoices", on_delete=models.CASCADE, null=True, blank=True)
    book_type = models.ForeignKey("books.BookType", on_delete=models.CASCADE, null=True, blank=True)
    is_free = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)


