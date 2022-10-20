from django.db import models


# Create your models here.
class Result(models.Model):
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, blank=True)
    order_id = models.ForeignKey("connections.Order", on_delete=models.CASCADE, null=True, blank=True)
    answer_id = models.ForeignKey("tests.Answers", on_delete=models.CASCADE, null=True, blank=True)
    question_id = models.ForeignKey("tests.Test", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)
