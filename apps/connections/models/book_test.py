from django.db import models


class BookTest(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey("books.Book", on_delete=models.CASCADE, null=True, blank=True)
    test_id = models.ForeignKey("tests.Test", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)
