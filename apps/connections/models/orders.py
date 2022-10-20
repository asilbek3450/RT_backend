from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, blank=True)
    book_id = models.ForeignKey("books.Book", on_delete=models.CASCADE, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)
